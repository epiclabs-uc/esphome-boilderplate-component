#pragma once
#include "esphome/core/component.h"
namespace esphome {
namespace boilerplate {
using namespace std;

class Boilerplate : public Component {
  void setup() override;
  void loop() override;
};

}  // namespace boilerplate
}  // namespace esphome