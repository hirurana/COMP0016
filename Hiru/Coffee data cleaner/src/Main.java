import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        System.out.println("ServerAPI Entitlement Verification");
        EntitlementVerification v = new EntitlementVerification();
        v.run();
        System.out.println("Press ENTER to quit");
        System.in.read();
    }
}
