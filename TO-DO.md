Use this for css:
https://github.com/Jeweleni/openai-summarizer 

Here are several gesture ideas that are simple, intuitive, and can be detected robustly with the camera:

### 1. **Swipe Gestures (Horizontal and Vertical Swipes)**:
   - **Horizontal Swipe (Left to Right)**: Swipe your hand horizontally from left to right to increase the volume.
   - **Horizontal Swipe (Right to Left)**: Swipe your hand horizontally from right to left to decrease the volume.
   - **Vertical Swipe (Up)**: Swipe your hand vertically upward to increase brightness or another control.
   - **Vertical Swipe (Down)**: Swipe your hand vertically downward to decrease brightness or another control.

   **Pros**:
   - Simple to implement.
   - Low likelihood of false positives.
   - Can be extended to control multiple functions (volume, brightness, etc.).

   **Cons**:
   - Requires clear, deliberate swipes for detection.

### 2. **Pinch-to-Zoom Gesture**:
   - **Pinch Fingers Together**: Move thumb and index finger closer together to decrease the volume.
   - **Spread Fingers Apart**: Move thumb and index finger away from each other to increase the volume.

   **Pros**:
   - Familiar gesture for most users (similar to zoom gestures on touch devices).
   - Precise control over volume adjustment.

   **Cons**:
   - Requires precise tracking of finger movements.
   - May need to adjust sensitivity to avoid unintentional activation.

### 3. **Hold and Move Gesture**:
   - **Hold Gesture (Hold Hand in Position and Move)**:
     - Hold your hand in front of the camera and move it up to increase volume, or down to decrease volume.
     - This gesture could be detected by tracking the movement of the palm or the center point between the thumb and index finger.

   **Pros**:
   - Easy to perform and detect.
   - Minimizes accidental volume changes as it requires both holding and moving.

   **Cons**:
   - Requires continuous tracking and may be less responsive if the hand moves too slowly or quickly.

### 4. **Hand Rotation Gesture (Simplified)**:
   - **Hand Tilt**: Instead of complex rotation, you can detect when the user tilts their hand up or down:
     - Tilt the hand up to increase volume.
     - Tilt the hand down to decrease volume.
   - This gesture can be detected by tracking the orientation of the palm or the angle between the thumb and index finger.

   **Pros**:
   - Easier to perform than a full rotation.
   - Intuitive and natural motion.

   **Cons**:
   - May require calibration to ensure it works across different hand positions and angles.

### 5. **Finger Counting Gesture**:
   - **Number of Fingers Shown**: Control the volume based on the number of fingers extended:
     - 1 Finger: Mute the volume.
     - 2 Fingers: Low volume.
     - 3 Fingers: Medium volume.
     - 4 Fingers: High volume.
     - 5 Fingers: Max volume.

   **Pros**:
   - Simple and intuitive; easy to remember.
   - Low chance of false positives as it requires deliberate actions.

   **Cons**:
   - Limited precision (only set volume to predefined levels).
   - Might not be as responsive for small adjustments.

### 6. **Double Tap Gesture**:
   - **Double Tap in Air**: The user taps the index finger against the thumb twice quickly to toggle between muting and unmuting the volume.
   - This could be combined with other gestures like swipe or hold to adjust the volume incrementally.

   **Pros**:
   - Distinct gesture, less likely to be performed accidentally.
   - Simple and effective for toggling states (e.g., mute/unmute).

   **Cons**:
   - Requires precise detection of the tapping motion.
   - Could be sensitive to speed or angle of the tap.

### 7. **Fist to Open Hand Gesture**:
   - **Fist to Open Hand**:
     - Start with a closed fist and then open your hand fully to increase the volume.
     - Reverse the gesture (open hand to fist) to decrease the volume.

   **Pros**:
   - Very intuitive and easy to detect.
   - Clear and distinct from other hand motions.

   **Cons**:
   - Requires continuous tracking of the hand shape.
   - May be less responsive if the gesture is performed too quickly or slowly.

### 8. **Wave Gesture**:
   - **Wave Left to Right**: A quick wave from left to right to increase the volume.
   - **Wave Right to Left**: A quick wave from right to left to decrease the volume.

   **Pros**:
   - Highly responsive and simple to perform.
   - Good for quick adjustments.

   **Cons**:
   - Could be prone to false positives if similar motions are detected.

### 9. **Clapping Gesture**:
   - **Single Clap**: Clap your hands once to toggle the volume between mute and the previous level.
   - **Double Clap**: Clap twice to increase the volume significantly.

   **Pros**:
   - Distinct and easy to perform.
   - Unlikely to trigger accidentally in most cases.

   **Cons**:
   - Requires sound detection and may be influenced by background noise.

### 10. **Thumbs Up / Thumbs Down Gesture**:
   - **Thumbs Up**: Perform a thumbs-up gesture to increase the volume.
   - **Thumbs Down**: Perform a thumbs-down gesture to decrease the volume.

   **Pros**:
   - Easy to perform and recognize.
   - Intuitive and widely understood gestures.

   **Cons**:
   - Might need precise angle detection to differentiate from other gestures.
