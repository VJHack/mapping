# mapping

Mapping obstacles (other cars) and barriers.

## Process<br/>
1. Begins with batch of sampleBarriers and sampleObs
2. Immediate batches plotted on local
3. Batches translated accounting for car position and heading
4. Translations and accumulated barrier batches plotted on global
<br/>

## Data Recieved<br/>
Barriers: 2D array with format [ [x1, y1, x2, y1], [x1, y1, x2, y1] ] <-- 2 line segments<br/>
Obstacles: 2D array with format [ [x, y, r] , [x, y, r] ] <-- 2 obstacles, r = size<br/>
Vehicle state: 1D array with format [x, y, angle] <-- ANGLE EXPRESSED IN RADIANS<br/>
<br/>

## Data Outputted<br/>
Local Plot: Array of immediate barriers and obstacles<br/>
Global Plot: Array of barriers aggregated overtime (to be tested)<br/>
<br/>

## Note<br/>
The initial side is at 90 degrees instead of 0 because the local plot arrow always points north. 
<br/>

## Example<br/>
In the before image, heading is 0. In the after image, the car has turned right (-90 degrees) and heading is now -90 degrees. The values in the barrier array change and are reflected in the local plot. The global plot reflects the change in heading. 

Although they work, this simple example does not demonstrate change in vehicle position nor were adjustments to the obstacle positions made. Yeah.
<br/>

![Before](https://github.com/WisconsinAutonomous/mapping/blob/master/Before.png)
![After](https://github.com/WisconsinAutonomous/mapping/blob/master/After.png)

