# Raspberry Pager

An IoT pager for the modern era.

Still a work in progress. Check back in a few months.

## WIP

This repo will end up holding:

- first-hand testimonial of how it works, battery life, etc
- cad and stl files for an enclosure
- a BOM for hardware purchase
- a hardware build guide
- tagged releases with build artifacts
- source code for the agent on the pi
- a software guide for the configuration of the agent
- (potentially) infrastructure code for the cloud pieces

The physical device has the following features:

- usb port for charging
- power switch (note that you can charge while the power is on or off)
- 1.3" IPS color LCD (240x240px)
- 4 buttons
- a 1W speaker

After it's fully configured, the main feature of the device is that when an incident happens, it'll let you know. And it'll provide you some basic ways to provide feedback to your on-call service.

Some ideas for user configuration:

- custom sound effect
- volume control (hardware potentiometer?)
- screen brightness
- screen rotation
- UI scale?
- sleep delay
- a debug menu! version info...

And the necessary agent configuration:

- wifi connection settings
- user credentials to on-call service
- (potentially) mqtt broker credentials

The communication model is ideally very simple, an API token or similar and the agent can ping the on-call service every so often for updates.

If that doesn't work, maybe the device can run an email client, and we can have an email server set up in AWS that lets the device receive email. Then the on-call service sends email, and the device polls every so often for new messages from its server. Probably lower latency than the API token idea, but still within acceptable limits. Just gotta learn how to set up an email server and client.

If it doesn't work to put email on the device (for power reasons or something), we can fall back to IoT. The device listens to AWS IoT over MQTT. AWS munges incoming email or SMS and puts it into IoT. This is the most brittle (more parts that can break), but again, maybe the lowest-power solution? Don't optimize for power yet, you don't know how much this thing draws anyway.
