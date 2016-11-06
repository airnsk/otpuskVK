function NumDay (day,mon,year) {
 var monthdey=new Array (12);
 monthdey[0]=31;monthdey[1]=28;monthdey[2]=31;
 monthdey[3]=30;monthdey[4]=31;monthdey[5]=30;
 monthdey[6]=31;monthdey[7]=31;monthdey[8]=30;
 monthdey[9]=31;monthdey[10]=30;monthdey[11]=31;
 if ((year%4==0) && (year%100!=0) || (year%400==0)) monthdey[1]=29;

 var a=0;
 for (var i=1; i<mon; i++) a+=monthdey[i-1];
 a+=day;
 return a;
}




