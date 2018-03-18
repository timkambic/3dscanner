// laser holder
difference(){
	linear_extrude(height = 18, center = true, convexity = 14, twist = 0)hull(){
		square([10,20]);
		translate([25,5,0]) circle(5);
		translate([25,15,0]) circle(5);
	}
	translate([10,25,0])rotate([90,0,0])cylinder(30,6,6);
	translate([22,10,-10]) cylinder(20,5,4);
	color("red")translate([3,-5,15.5]) rotate([0,45,0]) cube([10,30,10]);
	color("red")translate([0,-1,-1.5])cube([5,22,3]);
}

