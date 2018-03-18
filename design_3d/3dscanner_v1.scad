
cam_x = 40;
cam_y = 25;

translate([5,2.5,7.5]) color("red") cube([cam_x,cam_y,30]);

cube([cam_x+10,cam_y+5,7.5]);

paths = [[0,0],[3,10],[17,10],[20,0]];
difference(){
    color("green") rotate([-90,0,90]) translate([10,-10,50]){
        linear_extrude(height = 100, center = true, convexity = 14, twist = 0) 
        polygon(paths);
    }
    color("blue") translate([-95,17,-5]) cube([40,5,17]);
    color("purple") translate([0,7,7.5])rotate([0,-86,0]) cube([5,25,40]);
}

translate([0,-40,0]){
    difference(){
        cube([30,20,16]);
        translate([10,25,8])rotate([90,0,0])cylinder(30,6,6);
    }
}
