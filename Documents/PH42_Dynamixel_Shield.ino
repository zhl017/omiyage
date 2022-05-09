#include <DynamixelShield.h>

const uint8_t PH42_ID = 1;

DynamixelShield dxl;
//This namespace is required to use Control table item names
using namespace ControlTableItem;

uint32_t position1 = 0;       //center
uint32_t position2 = 303000;  //180 degree

void setup() {
  // put your setup code here, to run once:
  dxl.begin(57600);
  dxl.scan();
  dxl.torqueOn(PH42_ID);
}

void loop() {
  // put your main code here, to run repeatedly:
  //  dxl.setGoalPosition(PH42_ID, position2);
  dxl.writeControlTableItem(GOAL_POSITION, PH42_ID, position2);
  delay(100);
  while (dxl.readControlTableItem(MOVING, PH42_ID));

  
  dxl.writeControlTableItem(GOAL_POSITION, PH42_ID, -position2);
  delay(100);
  while (dxl.readControlTableItem(MOVING, PH42_ID));

  
  dxl.writeControlTableItem(GOAL_POSITION, PH42_ID, position1);
  delay(100);
  while (dxl.readControlTableItem(MOVING, PH42_ID));
}
