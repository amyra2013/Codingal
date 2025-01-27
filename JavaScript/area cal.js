var ask=prompt("Welcome to Area Calculator!Please choose a shape for which you would like to calculate the area:\n1.Rectangle\n2.Triangle\n3.Circle\n4.Parallelogram")

if (ask=='1') {
    l=prompt("Enter the length of the rectangle.")
    b=prompt("Enter the breadth of the rectangle.")
    var r_result=Number(l)*Number(b)
    alert("The area of this rectangle is"+r_result)
}

else if (ask=='2') {
    var hOfT=prompt("Enter the height of the triangle.")
    var bOfT=prompt("Enter the base of the triangle.")
    var t_result=Number(hOfT)*Number(bOfT)/2
    alert("The area of this triangle is"+t_result)
}

else if (ask=='3') {
    var r=prompt("Enter the radius of the circle.")
    var c_result=Number(r)*Number(r)*3.14
    alert("The area of this circle is"+c_result)
}

else if(ask=='4') {
    var hOfP=prompt("Enter the height of the parallelogram.")
    var bOfP=prompt("Enter the base of the parallelogram.")
    var p_result=Number(hOfP)*Number(bOfP)
    alert("The area of this parallelogram is"+p_result)
}



