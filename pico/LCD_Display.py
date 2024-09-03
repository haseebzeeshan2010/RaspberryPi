# LCD1602 and Pi Pico!

#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 10, 9, 8, 7);

void setup() {
  lcd.begin(16, 2);
  lcd.print("Hello World!");

  lcd.setCursor(2, 1);
  lcd.print("> Pi Pico <");
}

void loop() {

  lcd.begin(16, 2);
  lcd.print("Everything is");

  lcd.setCursor(2, 1);
  lcd.print("> POSSIBLE <");
  delay(2000);
  lcd.begin(16, 2);
  lcd.print("Believe in ");

  lcd.setCursor(2, 1);
  lcd.print("> YOURSELF <");
  delay(2000);

}
