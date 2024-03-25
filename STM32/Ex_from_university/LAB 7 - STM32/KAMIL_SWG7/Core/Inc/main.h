/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define B1_Pin GPIO_PIN_13
#define B1_GPIO_Port GPIOC
#define G_Pin GPIO_PIN_0
#define G_GPIO_Port GPIOC
#define D_Pin GPIO_PIN_1
#define D_GPIO_Port GPIOC
#define E_Pin GPIO_PIN_2
#define E_GPIO_Port GPIOC
#define C_Pin GPIO_PIN_3
#define C_GPIO_Port GPIOC
#define PHOTORESISTOR_Pin GPIO_PIN_1
#define PHOTORESISTOR_GPIO_Port GPIOA
#define USART_TX_Pin GPIO_PIN_2
#define USART_TX_GPIO_Port GPIOA
#define USART_RX_Pin GPIO_PIN_3
#define USART_RX_GPIO_Port GPIOA
#define CS_Pin GPIO_PIN_4
#define CS_GPIO_Port GPIOA
#define LD2_Pin GPIO_PIN_5
#define LD2_GPIO_Port GPIOA
#define B_Pin GPIO_PIN_4
#define B_GPIO_Port GPIOC
#define F_Pin GPIO_PIN_5
#define F_GPIO_Port GPIOC
#define S1_Pin GPIO_PIN_0
#define S1_GPIO_Port GPIOB
#define S1_EXTI_IRQn EXTI0_IRQn
#define A_Pin GPIO_PIN_6
#define A_GPIO_Port GPIOC
#define COM4_Pin GPIO_PIN_8
#define COM4_GPIO_Port GPIOC
#define COM3_Pin GPIO_PIN_9
#define COM3_GPIO_Port GPIOC
#define TMS_Pin GPIO_PIN_13
#define TMS_GPIO_Port GPIOA
#define TCK_Pin GPIO_PIN_14
#define TCK_GPIO_Port GPIOA
#define COM2_Pin GPIO_PIN_10
#define COM2_GPIO_Port GPIOC
#define COM1_Pin GPIO_PIN_11
#define COM1_GPIO_Port GPIOC
#define S2_Pin GPIO_PIN_5
#define S2_GPIO_Port GPIOB
#define S2_EXTI_IRQn EXTI9_5_IRQn
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
