#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino_JSON.h>
// WIFI info
const char* ssid = "Inteli-COLLEGE";
const char* password = "QazWsx@123";

char t = 'o'

//Your Domain name with URL path or IP address with path
String serverName = "https://w89zmz-3020.preview.csb.app/player1";

unsigned long lastTime = 0;

unsigned long timerDelay = 5000;

int greenLed = 3;
int redLed = 18;

void setup() {
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);

  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.println("Connecting");

  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}
void loop() {
  if(t = 'o'){
    serverName = "https://w89zmz-3020.preview.csb.app/player1";
    t ='h';
  }else}{ serverName = "https://w89zmz-3020.preview.csb.app/player2";t='0'}
  //Send an HTTP POST request every 10 minutes
  if ((millis() - lastTime) > timerDelay) {
    //Check WiFi connection status
    if(WiFi.status() == WL_CONNECTED){
      HTTPClient http;
      String serverPath = serverName;
      // Your Domain name with URL path or IP address with path
      http.begin(serverPath.c_str());

      // Send HTTP GET request
      int httpResponseCode = http.GET();
      if (httpResponseCode>0) {

        String payload = http.getString();
        Serial.println(payload);

        JSONVar myObject = JSON.parse(payload);
        JSONVar keys = myObject.keys();

        int p1 = int(myObject[keys[0]]);
        int p2 = int(myObject[keys[1]]);


        if(p1 < 0) {
          digitalWrite(greenLed, HIGH);
        } else {
          digitalWrite(greenLed, LOW);
        }
        if(p2 <0) {
          digitalWrite(redLed, HIGH);
        } else {
          digitalWrite(redLed, LOW);
        }
      }
      else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
      }
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
}