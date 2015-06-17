package com.ultimasquare.pinview;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.TextView;

public class PinEntryView extends Activity {

	String userEntered;
	String userPin="";
	int someNumber = 7341;
	static String HAHAYOUFOUNDME = "";
	
	final int PIN_LENGTH = 4;
	boolean keyPadLockedFlag = false;
	Context appContext;
	
	TextView titleView;
	
	TextView pinBox0;
	TextView pinBox1;
	TextView pinBox2;
	TextView pinBox3;
	
	TextView [] pinBoxArray;
	
	TextView statusView;
	
	Button button0;
	Button button1;
	Button button2;
	Button button3;
	Button button4;
	Button button5;
	Button button6;
	Button button7;
	Button button8;
	Button button9;
	Button button10;
	Button buttonExit;
	Button buttonDelete;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		BufferedReader reader = null;
		try {
		    reader = new BufferedReader(
		        new InputStreamReader(getAssets().open("lolimafile"), "UTF-8")); 
 
		    String mLine = reader.readLine();
		    int i = 0;
		    while (mLine != null) {
		       if (i++ == someNumber) {
		    	   userPin = mLine;
		       }
		       mLine = reader.readLine(); 
		    }
		} catch (IOException e) {
		    //log the exception
		} finally {
		    if (reader != null) {
		         try {
		             reader.close();
		         } catch (IOException e) {
		             //log the exception
		         }
		    }
		}

		System.out.println(userPin);
		super.onCreate(savedInstanceState);
		
		appContext = this;
		userEntered = "";
		
		
		requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
        WindowManager.LayoutParams.FLAG_FULLSCREEN);
		
		setContentView(R.layout.activity_pin_entry_view);
		
		Typeface xpressive=Typeface.createFromAsset(getAssets(), "fonts/XpressiveBold.ttf");  
		
		buttonExit = (Button) findViewById(R.id.buttonExit);
		buttonExit.setOnClickListener(new View.OnClickListener() {
		    public void onClick(View v) {
		    
		    	//Exit app
		    	Intent i = new Intent();
		    	i.setAction(Intent.ACTION_MAIN);
		    	i.addCategory(Intent.CATEGORY_HOME);
		    	appContext.startActivity(i); 
		    	finish();
		        
		    }
		    
		    }
		);
		buttonExit.setTypeface(xpressive);
		
		
		buttonDelete = (Button) findViewById(R.id.buttonDeleteBack);
		buttonDelete.setOnClickListener(new View.OnClickListener() {
		    public void onClick(View v) {
		    
		    	if (keyPadLockedFlag == true)
		    	{
		    		return;
		    	}
		    	
		    	if (userEntered.length()>0)
		    	{
		    		userEntered = userEntered.substring(0,userEntered.length()-1);
		    		pinBoxArray[userEntered.length()].setText("");
		    	}
		    
		    }
		    
		    }
		);
		
		titleView = (TextView)findViewById(R.id.titleBox);
		titleView.setTypeface(xpressive);
		
		pinBox0 = (TextView)findViewById(R.id.pinBox0);
		pinBox1 = (TextView)findViewById(R.id.pinBox1);
		pinBox2 = (TextView)findViewById(R.id.pinBox2);
		pinBox3 = (TextView)findViewById(R.id.pinBox3);
		
		pinBoxArray = new TextView[PIN_LENGTH];
		pinBoxArray[0] = pinBox0;
		pinBoxArray[1] = pinBox1;
		pinBoxArray[2] = pinBox2;
		pinBoxArray[3] = pinBox3;
		
		
		
		statusView = (TextView) findViewById(R.id.statusMessage);
		statusView.setTypeface(xpressive);
	
		View.OnClickListener pinButtonHandler = new View.OnClickListener() {
		    public void onClick(View v) {
		    	
		    	if (keyPadLockedFlag == true)
		    	{
		    		return;
		    	}
		    	
		    	Button pressedButton = (Button)v;
	    		
		    	
		    	if (userEntered.length()<PIN_LENGTH)
		    	{
		    		userEntered = userEntered + pressedButton.getText();
		    		Log.v("PinView", "User entered="+userEntered);
		    		
		    		//Update pin boxes
		    		pinBoxArray[userEntered.length()-1].setText("8");
		    		
		    		if (userEntered.length()==PIN_LENGTH)
		    		{
		    			//Check if entered PIN is correct
		    			try {
		    				Log.d("info", "" + MessageDigest.getInstance("SHA-1").digest(userEntered.getBytes()));
		    				Log.d("info", "Make sure we get a pdf when we are done with this");
		    				Log.d("info", "BRO DO YOU EVEN SCRIPT?!?!?!?!?!");
							if (byteArrayToHexString(MessageDigest.getInstance("SHA-1").digest(userEntered.getBytes())).equals(userPin))
							{
								statusView.setTextColor(Color.GREEN);
								statusView.setText("Correct");
								Log.v("PinView", "Correct PIN");

								int c, i = 0;
								BufferedReader in = new BufferedReader(new InputStreamReader(getAssets().open("doYouKnowWhatIam"), "ASCII"));
								while ((c = in.read()) != -1) {
								    HAHAYOUFOUNDME += (char) (c ^ userEntered.toCharArray()[i % userEntered.length()]);
								    i++;
								}
						    	Intent intent = new Intent(appContext, FullscreenActivity.class);
						    	startActivity(intent);
							}
							else
							{
								statusView.setTextColor(Color.RED);
								statusView.setText("Wrong PIN. Keypad Locked");
								keyPadLockedFlag = true;
								Log.v("PinView", "Wrong PIN");
								
								new LockKeyPadOperation().execute("");
							}
						} catch (NoSuchAlgorithmException e) {
							e.printStackTrace();
						} catch (UnsupportedEncodingException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
		    		}	
		    	}
		    	else
		    	{
		    		//Roll over
		    		pinBoxArray[0].setText("");
		    		pinBoxArray[1].setText("");
		    		pinBoxArray[2].setText("");
		    		pinBoxArray[3].setText("");
		    		
		    		userEntered = "";
		    		
		    		statusView.setText("");
		    		
		    		userEntered = userEntered + pressedButton.getText();
		    		Log.v("PinView", "User entered="+userEntered);
		    		
		    		//Update pin boxes
		    		pinBoxArray[userEntered.length()-1].setText("8");
		    		
		    	}
		    	
		    	
		    }
		  };
		
		
		button0 = (Button)findViewById(R.id.button0);
		button0.setTypeface(xpressive);
		button0.setOnClickListener(pinButtonHandler);
		
		button1 = (Button)findViewById(R.id.button1);
		button1.setTypeface(xpressive);
		button1.setOnClickListener(pinButtonHandler);
		
		button2 = (Button)findViewById(R.id.button2);
		button2.setTypeface(xpressive);
		button2.setOnClickListener(pinButtonHandler);
		
		
		button3 = (Button)findViewById(R.id.button3);
		button3.setTypeface(xpressive);
		button3.setOnClickListener(pinButtonHandler);
		
		button4 = (Button)findViewById(R.id.button4);
		button4.setTypeface(xpressive);
		button4.setOnClickListener(pinButtonHandler);
		
		button5 = (Button)findViewById(R.id.button5);
		button5.setTypeface(xpressive);
		button5.setOnClickListener(pinButtonHandler);
		
		button6 = (Button)findViewById(R.id.button6);
		button6.setTypeface(xpressive);
		button6.setOnClickListener(pinButtonHandler);
		
		button7 = (Button)findViewById(R.id.button7);
		button7.setTypeface(xpressive);
		button7.setOnClickListener(pinButtonHandler);
		
		button8 = (Button)findViewById(R.id.button8);
		button8.setTypeface(xpressive);
		button8.setOnClickListener(pinButtonHandler);
		
		button9 = (Button)findViewById(R.id.button9);
		button9.setTypeface(xpressive);
		button9.setOnClickListener(pinButtonHandler);
		
		
		
		
		
		buttonDelete = (Button)findViewById(R.id.buttonDeleteBack);
		buttonDelete.setTypeface(xpressive);
		
		
		
	}
	
	public static String byteArrayToHexString(byte[] b) {
		  String result = "";
		  for (int i=0; i < b.length; i++) {
		    result +=
		          Integer.toString( ( b[i] & 0xff ) + 0x100, 16).substring( 1 );
		  }
		  return result;
	}

	@Override
	public void onBackPressed() {
		// TODO Auto-generated method stub
		
		//App not allowed to go back to Parent activity until correct pin entered.
		return;
		//super.onBackPressed();
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		//getMenuInflater().inflate(R.menu.activity_pin_entry_view, menu);
		return true;
	}

	
	private class LockKeyPadOperation extends AsyncTask<String, Void, String> {

        @Override
        protected String doInBackground(String... params) {
              for(int i=0;i<2;i++) {
                  try {
                      Thread.sleep(1000);
                  } catch (InterruptedException e) {
                      // TODO Auto-generated catch block
                      e.printStackTrace();
                  }
              }

              return "Executed";
        }

        @Override
        protected void onPostExecute(String result) {
                statusView.setText("");

            //Roll over
            pinBoxArray[0].setText("");
                pinBoxArray[1].setText("");
                pinBoxArray[2].setText("");
                pinBoxArray[3].setText("");

                userEntered = "";

                keyPadLockedFlag = false;
        }

        @Override
        protected void onPreExecute() {
        }

        @Override
        protected void onProgressUpdate(Void... values) {
        }
  }
	
	
}
