/*
 * Servo.c
 *
 *  Created on: Nov 18, 2023
 *      Author: majka
 */

#include "Servo.h"
#include "main.h"


TIM_HandleTypeDef *ptr;
uint32_t channel;

void Servo_Init(TIM_HandleTypeDef *ptr_Servo,uint32_t channel_Servo){
	ptr = ptr_Servo;
	channel = channel_Servo;

	__HAL_TIM_SET_COMPARE(ptr,channel,SERVO_MIN_POS);
	HAL_TIM_PWM_Start(ptr, channel);

}

void Servo_set_angle(uint8_t angle){
	if(angle > SERVO_MAX_ANGLE){
		angle = SERVO_MAX_ANGLE;
	}else if(angle < SERVO_MIN_ANGLE){
		angle = SERVO_MIN_ANGLE;
	}
	Actual_angle_value = angle;
	uint32_t position = SERVO_MIN_POS + (angle * (SERVO_MAX_POS - SERVO_MIN_POS))/SERVO_MAX_ANGLE;
	__HAL_TIM_SET_COMPARE(ptr,channel,position);
}

void Servo_set_speed(uint8_t speed){
	if(speed < -SERVO_MAX_SPEED){
		speed = -SERVO_MAX_SPEED;
	}else if(speed > SERVO_MAX_SPEED){
		speed = SERVO_MAX_SPEED;
	}
	uint32_t position = (SERVO_MAX_POS + SERVO_MIN_POS)/2 + (speed * (SERVO_MAX_POS - SERVO_MIN_POS)/2)/SERVO_MAX_SPEED;

	__HAL_TIM_SET_COMPARE(ptr, channel, position);
}
