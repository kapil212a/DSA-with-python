public class ds {
    public static void printarr(int arr[]){
        for(int i = 0 ;i<arr.length; i++){
            System.err.print(arr[i]+" ");
        }
    }
    public static void reverse(int arr[]){
        int start = 0;
        int end = arr.length-1;
        while(start<end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    public static void main(String[] args) {
        // int m = 40;

        // int n = 50;
        // int c = m/n;
        // System.out.println("fraction form of" + m +"/" + n);
        int arr[] = {1,2,3,4,5};
        reverse(arr);
        printarr(arr);

        
    }
}
