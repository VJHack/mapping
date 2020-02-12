# mapping

Mapping obstacles (other cars) and barriers.

### Process
1. Begins with array of sampleBarriers and sampleObs
2. Immediate (surronding) arrays get plotted on local
3. Arrays get translated, accounting for car position and heading
4. Translations and accumulated barrier array get plotted on global

### Data Recieved
Barriers: 2D array with format [ [x1, y1, x2, y1], [x1, y1, x2, y1] ] <-- 2 line segments<br/>
Obstacles: 2D array with format [ [x, y, r] , [x, y, r] ] <-- 2 obstacles, r = size<br/>
Vehicle state: 1D array with format [x, y, angle] <-- ANGLE EXPRESSED IN RADIANS<br/>

### Data Outputted
Local Plot: Array of immediate barriers and obstacles<br/>
Global Plot: Array of barriers aggregated overtime (to be tested)<br/>

### Note
The initial side is at 90 degrees instead of 0 because the local plot arrow always points north. 

### Example
In the before (top) image, heading is 0. In the after (bottom) image, the car has turned right (-90 degrees) and heading is now -90 degrees. The values in the barrier array change and are reflected in the local plot. The global plot reflects the change in heading. 

Although they work, this simple example does not demonstrate change in vehicle position nor were adjustments to the obstacle positions made. Yeah.
<br/>

![Before](https://github.com/WisconsinAutonomous/mapping/blob/master/Before.png)
![After](https://github.com/WisconsinAutonomous/mapping/blob/master/After.png)

