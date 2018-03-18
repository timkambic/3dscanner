
// legs
difference(){
union(){
	color("gray")translate([0,0,-10.25])rotate([0,0,30])cube([140,7,15.5],true);
	color("gray")translate([0,0,-10.25])rotate([0,0,-30])cube([140,7,15.5],true);

	color("lime")hull(){
		translate([0,0,-7])cube([60,40,2], true);
		translate([0,0,-17])cylinder(1,10,10,true);
	}
	translate([0,0,-5])cube([60,40,5], true);


	rotate([0,0,30])translate([67,0,-20])cylinder(2,3,3);
	rotate([0,0,30])translate([-67,0,-20])cylinder(2,3,3);
	rotate([0,0,-30])translate([67,0,-20])cylinder(2,3,3);
	rotate([0,0,-30])translate([-67,0,-20])cylinder(2,3,3);


	color("green")translate([-12.5,-25,-15.5])cube([25,50,13]);
}
rotate([90,0,0])translate([0,-9,0])cylinder(60,4,4,true);
}
	



// MOTOR HOLDER 
translate([0,-130,-4]){
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

		rotate([90,0,0])translate([0,-5,0])cylinder(60,4,4,true);
	}
}
//floor
*color("olive")translate([0,0,-25])cube([300,300,10],true);

// screw
*color("blue")rotate([90,0,0])translate([0,-9,50])cylinder(300,4,4,true);
		



