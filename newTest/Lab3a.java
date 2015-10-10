public class Lab3a{
	public static void main(String[] args){
		double distance = 10.0;
		int count = 0;
		while(distance!=0){
			distance/=2;
			count++;
		}
		System.out.printf("%f \n",distance );
		System.out.println("The number of steps taken is: " + count);
	}

}