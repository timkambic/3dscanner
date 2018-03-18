
difference(){
	scale([1.1,1])cylinder(24, 20,20);

	color("blue")translate([0,0,5])linear_extrude(height = 19.3, center = false){
		circle(14);
		translate([0,8,0])square([17.5,10],true);
		translate([0,15,0]) square([15,10],true);
	}

	color("green")translate([0,0,15])linear_extrude(height = 10, center = false){
		translate([17,0,0])circle(2);
		translate([-17,0,0])circle(2);
	}
}

difference(){
translate([0,0,-16])linear_extrude(height = 20, center = false)hull(){
	scale([1.1,1])circle(20);
	translate([0,20,0])square([25,10],true);
	translate([0,-20,0])square([25,10],true);
}

rotate([90,0,0])translate([0,-5,0])cylinder(60,5,5,true);
}