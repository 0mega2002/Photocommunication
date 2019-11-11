int lmao = 1;
byte data[1024];
int pos = 0;

bool isFirst = true;
void setup() {
  // put your setup code here, to run once:
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(14, OUTPUT);
  pinMode(15, OUTPUT);
  pinMode(16, OUTPUT);
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  digitalWrite(11, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
  digitalWrite(14, HIGH);
  digitalWrite(15, HIGH);
  digitalWrite(16, HIGH);
  digitalWrite(17, HIGH);
  digitalWrite(18, HIGH);
  Serial.begin(115200);
}


void loop() {
  // put your main code here, to run repeatedly:
  int accc = digitalRead(9);
  if (accc == lmao) {
    delayMicroseconds(500);
    scriviser();
    lmao = 1 - accc;


  }
}

void scriviser() {
  int numero[6] = {0, 0, 0, 0, 0, 0};
  for (int porta = 0; porta < 6; porta++) {
    if ((1 - digitalRead(porta + 3)) == 0) {
      numero[porta] = 0;
    }
    else if ((1 - digitalRead(porta + 3)) == 1) {
      numero[porta] = 1;
    }
  }
  int numdec = (numero[0] * 1) + (numero[1] * 2) + (numero[2] * 2 * 2) + (numero[3] * 2 * 2 * 2) + (numero[4] * 2 * 2 * 2 * 2) + (numero[5] * 2 * 2 * 2 * 2 * 2);
  //Serial.print((char)trasf(numdec));
  if (digitalRead(10)) {
    data[pos] = trasf(numdec);
    pos++;
  }
  if (!digitalRead(10)) {
    data[pos] = trasf(numdec);

    for (int i = 0; i < pos + 1; i++) {
      if ((char)data[i] == 'A' && isFirst) {
        continue;
      }
      if ((char)data[i] != 'A') {
        if (isFirst) {
          isFirst = false;
        }
        if (!isFirst) {
          Serial.print((char)data[i]);
          if (i == pos) {
            Serial.println();
          }
        }
      }

    }

    memset(data, 0, 1024);
    pos = 0;
  }

}

byte trasf(int x) {
  if (x <= 25 && x >= 0) {
    int y = x + 65;
    return y;
  }
  if (x <= 51 && x >= 26) {
    int y = x + 71;
    return y;
  }
  if (x <= 61 && x >= 52) {
    int y = x - 4;
    return y;
  }
  if (x == 62) {
    int y = 43;
    return y;
  }
  if (x == 63) {
    int y = 47;
    return y;
  }

}
