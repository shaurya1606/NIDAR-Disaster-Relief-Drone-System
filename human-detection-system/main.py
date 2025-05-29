"""
Main Application for Human Detection System
"""
import signal
import time
from modules.sound_manager import SoundManager
from modules.camera_manager import CameraManager
from modules.detector import HumanDetector
from modules.display_manager import DisplayManager

# Global control flag
should_run = True

def signal_handler(signum, frame):
    """Handle cleanup when Ctrl+C is pressed"""
    global should_run
    print("\n👋 Caught interrupt signal. Cleaning up...")
    should_run = False

# Register the signal handler for Ctrl+C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

def main():
    try:
        # Initialize components
        sound_mgr = SoundManager()
        camera_mgr = CameraManager()
        detector = HumanDetector()
        display_mgr = DisplayManager()

        # Setup components
        sound_mgr.setup_sound()
        camera_mgr.setup_camera()
        
        # Initial camera connection
        try:
            camera_mgr.connect()
        except ConnectionError as e:
            print(f"\n❌ Failed to establish initial camera connection: {str(e)}")
            return
            
        detector.load_model()

        connection_retry_count = 0
        max_connection_retries = 3

        # Main processing loop
        while should_run:
            try:
                # Get frame from camera with error handling
                ret, frame = camera_mgr.read_frame()
                
                if not ret:
                    print("\n⚠️ Failed to read frame")
                    connection_retry_count += 1
                    
                    if connection_retry_count > max_connection_retries:
                        print("\n❌ Maximum connection retries exceeded. Exiting...")
                        break
                        
                    try:
                        if not camera_mgr.reconnect():
                            print("\n❌ Reconnection failed")
                            continue
                        connection_retry_count = 0
                    except ConnectionError as e:
                        print(f"\n❌ Reconnection error: {str(e)}")
                        continue
                        
                    continue

                # Reset retry counter on successful frame read
                connection_retry_count = 0

                # Process frame
                frame, detections = detector.detect_humans(frame)

                # Handle detections
                if detections > 0:
                    current_time = time.time()
                    if (current_time - sound_mgr.last_sound_time) >= sound_mgr.SOUND_COOLDOWN:
                        sound_mgr.play_alert_threaded()
                        sound_mgr.last_sound_time = current_time

                # Update display
                frame = display_mgr.add_fps(frame)
                frame = display_mgr.add_info(
                    frame,
                    detections,
                    camera_mgr.get_source_text(),
                    sound_mgr.get_alert_type_display()
                )

                # Save and show frame
                display_mgr.save_frame(frame, detections)
                display_mgr.show_frame(frame)

                # Check for quit
                if display_mgr.check_quit():
                    print("\n👋 Exiting...")
                    break

            except Exception as e:
                print(f"\n❌ Error in main loop: {str(e)}")
                time.sleep(1)  # Prevent rapid error loops
                continue

    except KeyboardInterrupt:
        print("\n👋 Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
    finally:
        # Cleanup
        print("\n🧹 Performing cleanup...")
        camera_mgr.release()
        print("✅ Cleanup completed successfully")

if __name__ == "__main__":
    main() 