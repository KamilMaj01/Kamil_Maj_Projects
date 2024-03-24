/*
 * Servo.h
 *
 *  Created on: Nov 18, 2023
 *      Author: majkamil
 */

#ifndef INC_SERVO_H_
#define INC_SERVO_H_

#include <stdint.h>
#include "stm32f4xx_hal.h"



#define SERVO_MAX_POS 2200
#define SERVO_MIN_POS 800
#define SERVO_MAX_ANGLE 125
#define SERVO_MIN_ANGLE 0
#define SERVO_MAX_SPEED 100

void Servo_Init(TIM_HandleTypeDef *,uint32_t);
void Servo_set_speed(uint8_t);
void Servo_set_angle(uint8_t);



#endif /* INC_SERVO_H_ */
