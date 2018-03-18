// camera
*translate([5,5,6]) cube([49,26,35.5]);

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

//laser arm
paths = [[0,0],[3,10],[17,10],[20,0]];
difference(){
    color("green") translate([-50,25,10]) rotate([90,180,90]){
        linear_extrude(height = 100, center = true, convexity = 14, twist = 0) 
        polygon(paths);
    }
    color("blue") translate([-95,12,-5]) cube([40,5,17]);
    *color("purple") translate([0,3,7.5])rotate([0,-86,0]) cube([5,25,40]);
}


// laser holder
translate([0,-80,8]){
    difference(){
        linear_extrude(height = 18, center = true, convexity = 14, twist = 0)hull(){
            square([10,20]);
            translate([25,5,0]) circle(5);
            translate([25,15,0]) circle(5);
        }
        translate([10,25,0])rotate([90,0,0])cylinder(30,6,6);
        translate([22,10,-10]) cylinder(20,5,4);
        color("red")translate([3,-5,15]) rotate([0,45,0]) cube([10,30,10]);
    }
    
}




//
scale_factor = 0.7;
path_base_pillar =[[-20.5,-20],[20.5,-20],[29.5,0],[20.5,20],[-20.5,20],[-30.5,0]];
translate([29.5,20,-50])linear_extrude(height = 50, center = false, convexity = 10, scale=scale_factor)
difference(){
	color("red") polygon(path_base_pillar);
	polygon(path_base_pillar*0.75);
	color("green")translate([0,18,0])square([32,10],true);
	color("green")translate([0,-18,0])square([26,10],true);
}
translate([29.5,20,-50])color("purple")translate([-13,-16,35])cube([26,4,15]);