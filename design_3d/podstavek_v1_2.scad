//baseplate
%translate([-29.5,-20,50])difference(){
	cube([59,40,6]);
	color("green")translate([26,17,-1]){
		cube([7,26,8]);
		translate([3.5,0,0])cylinder(8,3.5,3.5);
	}
}
scale_factor = 0.8;
path_base_pillar =[[-20.5,-20],[20.5,-20],[30.5,0],[20.5,20],[-20.5,20],[-30.5,0]];
// hexagonal pillars
translate([0,0,2]) linear_extrude(height = 50, center = false, convexity = 10, scale=scale_factor)
difference(){
	color("red") polygon(path_base_pillar);
	polygon(path_base_pillar*0.75);
	color("green")translate([0,18,0])square([32,10],true);
	color("green")translate([0,-18,0])square([26,10],true);
}
// linking block
color("purple")translate([-13,-16,37])cube([26,4,15]);

color("DarkKhaki")
translate([0,0,0])linear_extrude(height = 2, center = false, convexity = 10)
polygon(path_base_pillar);

color("steelblue")hull(){
	translate([0,0,-2])linear_extrude(height = 2, center = false, convexity = 10)
	polygon(path_base_pillar);
	translate([0,0,-6])cube([60,40,2], true);
}
// legs
color("gray")translate([0,0,-12])rotate([0,0,30])cube([140,7,12],true);
color("gray")translate([0,0,-12])rotate([0,0,-30])cube([140,7,12],true);

color("lime")hull(){
	translate([0,0,-7])cube([60,40,2], true);
	translate([0,0,-15])cylinder(1,10,10,true);
}



rotate([0,0,30])translate([67,0,-20])cylinder(2,3,3);
rotate([0,0,30])translate([-67,0,-20])cylinder(2,3,3);
rotate([0,0,-30])translate([67,0,-20])cylinder(2,3,3);
rotate([0,0,-30])translate([-67,0,-20])cylinder(2,3,3);
// linking to motor
/*
difference(){
	translate([0,-21,-12])cube([25,50,12],true);

	color("red") translate([0,-68,-18])
	linear_extrude(height = 12, center = false, convexity = 10)
	polygon([ [0,0], [8,30], [-8,30] ]);
}
*/

translate([-12.5,-45,-18])cube([25,50,12]);

color("red")translate([-12.5,-45,-6])cube([25,25,8]);
difference(){
	color("crimson")translate([-12.5,-45,2])cube([25,30,14]);
	translate([0,-15,7])rotate([90,0,0])cylinder(30,4,5);
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
color("olive")translate([0,0,-25])cube([300,300,10],true);

// screw
color("blue")rotate([90,0,0])translate([0,-9,50])cylinder(300,4,4,true);
		



