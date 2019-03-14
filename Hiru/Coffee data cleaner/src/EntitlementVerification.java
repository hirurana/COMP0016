import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.bloomberglp.blpapi.CorrelationID;
import com.bloomberglp.blpapi.Element;
import com.bloomberglp.blpapi.Event;
import com.bloomberglp.blpapi.EventHandler;
import com.bloomberglp.blpapi.Identity;
import com.bloomberglp.blpapi.Message;
import com.bloomberglp.blpapi.MessageIterator;
import com.bloomberglp.blpapi.Name;
import com.bloomberglp.blpapi.Request;
import com.bloomberglp.blpapi.EventQueue;
import com.bloomberglp.blpapi.Service;
import com.bloomberglp.blpapi.Session;
import com.bloomberglp.blpapi.SessionOptions;

public class EntitlementVerification {
    private String              d_host;
    private int                 d_port;
    private ArrayList<String>   d_securities;
    private int                 d_uuid;
    private ArrayList<Identity> d_users;
    private String              d_programAddress;

    private Session             d_session;
    private Service             d_apiAuthSvc;
    private Service             d_blpRefDataSvc;

    private static final Name SECURITY_DATA = Name.getName("securityData");
    private static final Name SECURITY = Name.getName("security");
    private static final Name EID_DATA = Name.getName("eidData");

    private static final String API_AUTH_SVC_NAME = "//blp/apiauth";
    private static final String REF_DATA_SVC_NAME = "//blp/refdata";

    public EntitlementVerification() {
        d_host = "localhost";
        d_port = 8194;
        d_uuid = 4683026;
        d_programAddress = "10.16.86.29";
    }

    public void run() throws IOException, InterruptedException {
        // Fill in the options
        SessionOptions options = new SessionOptions();
        options.setServerHost(d_host);
        options.setServerPort(d_port);

        System.out.println("Connecting to " + d_host + ":" + d_port);

        // create and start the session
        d_session = new Session(options);
        boolean sessionStarted = d_session.start();
        if (!sessionStarted) {
            System.err.println("Failed to start session. Exiting...");
            System.exit(-1);
        }
        // Open the services necessary
        if (!d_session.openService(API_AUTH_SVC_NAME)) {
            System.out.println("Failed to open service: " +
                    API_AUTH_SVC_NAME);
            System.exit(-1);
        }
        if (!d_session.openService(REF_DATA_SVC_NAME)) {
            System.out.println("Failed to open service: " +
                    REF_DATA_SVC_NAME);
            System.exit(-2);
        }

        d_apiAuthSvc  = d_session.getService(API_AUTH_SVC_NAME);
        d_blpRefDataSvc = d_session.getService(REF_DATA_SVC_NAME);

        // Authorize all the users that are interested in receiving data
        Identity Identity = d_session.createIdentity();
        Request authRequest = d_apiAuthSvc.createAuthorizationRequest();
        authRequest.set("uuid", d_uuid);
        authRequest.set("ipAddress", d_programAddress);
        CorrelationID correlator = new CorrelationID(d_uuid);
        d_session.sendAuthorizationRequest(authRequest, Identity,
                correlator);
        while(true){
            Event eventobj = d_session.nextEvent();
            if (eventobj.eventType() == Event.EventType.RESPONSE) {
                //Handle authorization response here
                break;
            }
        }
    }
}
