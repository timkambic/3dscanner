//laser arm
paths = [[0,0],[3,10],[17,10],[20,0]];
translate([-7,5,0]){
	difference(){
		color("green") translate([-50,25,10]) rotate([90,180,90]){
			linear_extrude(height = 100, center = true, convexity = 14, twist = 0) 
			polygon(paths);
		}
		color("blue") translate([-95,12,-5]) cube([50,5,17]);
		*color("purple") translate([0,3,7.5])rotate([0,-86,0]) cube([5,25,40]);
	}
}
color("lime")translate([-7,10,5])cube([7,20,5]);




