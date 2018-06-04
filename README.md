# arc

### What is it

A kit consisting of boards, sensors, and software that tracks sound levels which match those of abnormally high volume. The system is designed to automatically store sound values within a database, graphing, photos, video, and also has functionality which can approximate the origin when more than one device is implemented on premises.

### Why

The purpose is to provide an affordable, easy to implement device which can be utilized by entities that may not have the funding to purchase adequate security devices to monitor instances of increased activity in the area.

### Status

In-Dev, Unstable.
Currently fully functions to work only on the first sound detected.

### Setup

For the base testing model:

 - Sound Sensor [https://www.velleman.eu/products/view/?id=435532] Model: [VMA309]
 - LED Sensor [https://www.velleman.eu/products/view/?id=435550] Model: {VMA318]
 - Camera Module:<br>
  Amazon - [https://www.amazon.com/Kuman-Raspberry-Camera-Module-Supports/dp/B0759GYR51/ref=sr_1_8?ie=UTF8&qid=1527541394&sr=8-8&keywords=pi+camera] <br>
   Vendor - [http://www.kumantech.com/kuman-5mp-1080p-hd-camera-module-for-raspberry-pi-for-raspberry-pi-3-model-b-b-a-rpi-2-1-sc15_p0063.html] Model: [OV5647]

Run the python script.

Down the pipeline there are plans to make it boot directly into the arc, as well as a simple setup script that brings in all dependencies.

### Contributions

Feel free to add to this and create a pull request with your features, fixes, or other modifications.

### Video Examples


### Log Examples

`Setting up System...`<br>
`Setting up Database...`<br>
`Submitted logon to database`<br>
`Checking...`<br>
`Checking Database`<br>
`Database is Closed`<br>
`Checking...`<br>
`Checking...`<br>
`Checking...`<br>
`Sound detected 2018-05-27 03:55:12.857520`<br>
`Alert 2018-05-27 03:55:12.857520`<br>
`Initiated Camera`<br>
`Set Camera Resolution`<br>
`Started Camera Preview`<br>
`Checking...`<br>
`Checking Database`<br>
`Database is Closed`<br>
`Checking...`<br>
`Checking...`<br>
`Checking...`<br>
`Started Recording...`<br>
`Stopped Recording`<br>
`Stopped Preview`<br>
`Opened Video to prep for Database`<br>
`Encoded Video`<br>
`Set up qdb2 Cursor`<br>
`Created Insert String`<br>
`Inserted Query`<br>
`Sending Email Alert`<br>
`Checking...`<br>
`Checking...`<br>
`Checking...`<br>
`Checking...`<br>
`Sound detected 2018-05-27 03:55:17.646580`<br>
`Alert 2018-05-27 03:55:17.646580`<br>


