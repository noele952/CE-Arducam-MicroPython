# Arducam Mega 5MP Camera for Raspberry Pi Pico (Micropython)

**Forked Repository for Experimental Modifications**

This repository is a fork of the Core Electronics port of the Arducam Mega 5MP Camera for the Raspberry Pi Pico. The original project is marked as experimental, and frequent, breaking updates are expected.

## Changes Made

I created this fork of the Arducam driver to address specific needs in my Pico and Micropython-based hydroponic garden project. Two main issues prompted these modifications:

1. **Limited Storage Space on Hardware:**

   - Due to the limitations of the hardware I am using, the original driver's ability to save camera pictures at high resolutions was a concern because of the restricted storage space.

2. **Watchdog Timer and Image Saving Time:**

   - The `saveJPG` function from the original driver took longer than the maximum watchdog timer duration (approximately 8 seconds). This caused a reset of the machine due to the watchdog timer expiring.
   - To overcome this, I introduced a `generateJPG` function that returns the camera buffer data as a generator. This allows me to process the image incrementally, avoiding triggering the watchdog timer.
   - Additionally, as I upload images to the cloud via MQTT messages, the generator function enables asynchronous message sending using the asyncio library

3. **Cloud-Based Image Processing:**
   - Since the purpose of my modifications are to allow sending the image data into the cloud directly from the camera buffer, I removed the filemanager functions from the original driver.

## Original README

This is the Repo for the Core Electronics port of the Arducam Mega 5MP Camera for the Raspberry Pi Pico (Micropython)

Status: **Experimental**
This driver is very much experimental at the moment. Expect frequent, breaking updates.
This project is featured in the 27-July-2023 episode of [The Factory](https://youtu.be/M_b3kmnjF9Y) - Core Electronics' Engineering and Product Development vlog.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=M_b3kmnjF9Y" target="_blank">
 <img src="http://img.youtube.com/vi/M_b3kmnjF9Y/mqdefault.jpg" alt="Watch the video" width="240" height="180" border="10" />
</a>

Project Status:

- [ ] Confirmed working on 3MP Camera (ISSUE: Photos have a green hue, camera_idx identifies the two versions)
- [x] Can set resolution
- [ ] Can set remaining filters and modes
- [ ] Class moved to separate file
- [ ] Burst read
- [ ] Confirm a micro SD card can use the same SPI bus (Micropython compatibility)
- [ ] Confirm working with latest Micropython version)
- [ ] Filemanager also handles subfolders for images
- [ ] Confirm that different file formats output correctly (RGB=BMP, YGV?)
- [ ] Confirm that pixel RGB values can be extrapolated from BMP format for machine learning applications

# License

This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).
