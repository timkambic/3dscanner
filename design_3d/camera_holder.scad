scale([1.02,1.02,1.02]){
//baseplate
difference(){
	cube([59,40,6]);
	color("green")translate([26,17,-1]){
		cube([7,26,8]);
		translate([3.5,0,0])cylinder(8,3.5,3.5);
	}
}
//front wall
difference(){
	union(){
		color("green")translate([0,0,6])cube([59,3.5,5]);
		translate([0,0,11])cube([59,3.5,20]);
	}
	color("red") translate([29.5,4,23]) rotate([90,0,0])cylinder(5,11.5,11.5);
	color("blue") translate([18,-1,23])cube([23,5,20]);
}
//left wall
color("red")translate([0,0,6]){
	linear_extrude(height=15, center=false, convexity=14, twist=0)
	polygon( [ [0,0],[0,40],[4.6,40],[4.9,0] ] );
}
//right wall
color("red")translate([59,0,6]){
	linear_extrude(height=15, center=false, convexity=14, twist=0)
	polygon( [ [0,0],[0,40],[-4.6,40],[-4.9,0] ] );
}

//elastics mounting points
translate([14,-5,])cube([5,5,4]);
translate([40,-5,])cube([5,5,4]);
translate([14,40,])cube([5,5,4]);
translate([40,40,])cube([5,5,4]);


//arm mounting point
translate([-7,10,0])cube([7,20,5]);
}