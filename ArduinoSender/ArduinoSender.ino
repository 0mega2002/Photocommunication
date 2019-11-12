const int DEL = 1000;
int st = 0;
int acc = 1;
byte data[1024];
int pos = 0;
bool p = false;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  digitalWrite(9, HIGH);
}

//void loop() {
//  // put your main code here, to run repeatedly:
//  if (Serial.available()) {
//    int ch = Serial.read();
//    int numchar = (trasf(ch));
//    if (acc == 1){digitalWrite(9,LOW);acc = 0;}
//  else if (acc == 0){digitalWrite(9,HIGH);acc = 1;}
//    invio(numchar);
//
//    //Serial.println(ch);
//  }
//  for (int i = 5; i >= 0; i--) {
//    int porta = i + 3;
//    if (1) {
//      digitalWrite(porta, LOW);
//    }
//  }
//}

void loop() {
  while (Serial.available() > 0) {
    data[pos] = Serial.read();
    pos++;
  }
  
  if (pos > 0) {
    for (int i = 0; i < pos; i++) {
      if (acc == 1) {digitalWrite(9, LOW);acc = 0;}
      else if (acc == 0) {digitalWrite(9, HIGH);acc = 1;}
      if (i == pos-1)p=true;
      invio(trasf(data[i]));
      }
      
    }
    memset(data,0,1024);
    pos = 0;
    for (int i = 5; i >= 0; i--) {
      int porta = i + 3;
        digitalWrite(porta, LOW);
        digitalWrite(10,LOW);
    }
  }

void invio(int x) {
  int bin[6] = {0, 0, 0, 0, 0, 0};
  int i = 0;
  while (x > 0) {
    bin[i] = x % 2;
    x = x / 2;
    i++;
  }
  for (int i = 5; i >= 0; i--) {
    int porta = i + 3;
    if (bin[i] == 1) {
      digitalWrite(porta, HIGH);
    }
    else {
      digitalWrite(porta, LOW);
    }
    //Serial.print(bin[i]);
  }
  if (p){digitalWrite(10,HIGH);}  
 // Serial.println();
  delayMicroseconds(DEL);
  // IL 3 è LA PRIMA CIFRA A DESTRA(1), IL 10 è L'OTTAVA CIFRA(128)
}


int trasf(byte x) {
  if (x <= 90 && x >= 65) {
    int y = x - 65;               //caratteri maiuscoli
    return y;
  }
  if (x <= 122 && x >= 97) {
    int y = x - 71;              //caratteri minuscoli
    return y;
  }
  if (x <= 57 && x >= 48) {
    int y = x + 4;               //numeri
    return y;
  }
  if (x == 43) {
    int y = 62;                   //+
    return y;
  }
  if (x == 47) {
    int y = 63;                   //barra"/"
    return y;
  }

}
