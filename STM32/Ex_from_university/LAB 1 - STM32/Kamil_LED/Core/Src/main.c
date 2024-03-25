/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
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
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

// Funkcja umożliwiająca dynamiczną zmianę konfiguracji poszczególnych pinów miktrokontrolera 
void PINdir(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, uint8_t dir)
{
	GPIO_InitTypeDef GPIO_InitStruct = {0};
	switch(dir){
	// Rekonfiguracaja pinu jako wejście
	case 0:
		// Tworzenie struktury pinu
		GPIO_InitStruct.Pin = GPIO_Pin;
		GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
		GPIO_InitStruct.Pull = GPIO_NOPULL;
		HAL_GPIO_Init(GPIOx, &GPIO_InitStruct); // Przypisanie struktury do danego pinu
		break;
	// Rekonfiguracaja pinu jako wyjście
	case 1:
		GPIO_InitStruct.Pin = GPIO_Pin;
		GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
		GPIO_InitStruct.Pull = GPIO_NOPULL;
		GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
		HAL_GPIO_Init(GPIOx, &GPIO_InitStruct);
		break;
	// Rekonfiguracaja pinu jako wejście
	default:
		GPIO_InitStruct.Pin = GPIO_Pin;
		GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
		GPIO_InitStruct.Pull = GPIO_NOPULL;
		HAL_GPIO_Init(GPIOx, &GPIO_InitStruct);
		break;
	}


}

// funkcja umożliwiająca zaświecenie poszcególną diodą w 4 wariantach kolorystycznych
// Parametry:
// 		- LED - Przyjmuje wartości od 1 do 4. Określa na kórej diodzie RGB chcemy dokonać zmiany
//		- color - Określa na jaki kolor chcemy zaświecic diodę wybraną przez poprzedni parametr
//				gdzie:
//					1 - czerowny
//					2 - zielony
//					3 - niebieski
//					inny - biały
void LED(uint8_t LED, uint8_t color){
	if(LED == 1){
		if(color == 1){
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 0);
			PINdir(PB8_GPIO_Port, PB8_Pin, 0);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_RESET);
		}
		else if(color == 2){
			PINdir(PB6_GPIO_Port, PB6_Pin, 0);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 0);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_RESET);
		}
		else if(color == 3){
			PINdir(PB6_GPIO_Port, PB6_Pin, 0);
			PINdir(PB7_GPIO_Port, PB7_Pin, 0);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_RESET);
		}
		else{
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_RESET);
		}
	}
	if(LED == 2){
		if(color == 1){
			PINdir(PB6_GPIO_Port, PB6_Pin, 0);
			PINdir(PB7_GPIO_Port, PB7_Pin, 0);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_RESET);
		}
		else if(color == 2){
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 0);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 0);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_RESET);
		}
		else if(color == 3){
			PINdir(PB6_GPIO_Port, PB6_Pin, 0);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 0);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_RESET);
		}
		else{
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_RESET);
		}
	}
	if(LED == 3){
		if(color == 1){
			PINdir(PB6_GPIO_Port, PB6_Pin, 0);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 0);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_RESET);
		}
		else if(color == 2){
			PINdir(PB6_GPIO_Port, PB6_Pin, 0);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 0);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_RESET);
		}
		else if(color == 3){
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 0);
			PINdir(PB9_GPIO_Port, PB9_Pin, 0);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_RESET);
		}
		else{
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_RESET);
		}
	}
	if(LED == 4){
		if(color == 1){
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 0);
			PINdir(PB9_GPIO_Port, PB9_Pin, 0);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_RESET);
		}
		else if(color == 2){
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 0);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 0);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_RESET);
		}
		else if(color == 3){
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 0);
			PINdir(PB8_GPIO_Port, PB8_Pin, 0);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_RESET);
		}
		else{
			PINdir(PB6_GPIO_Port, PB6_Pin, 1);
			PINdir(PB7_GPIO_Port, PB7_Pin, 1);
			PINdir(PB8_GPIO_Port, PB8_Pin, 1);
			PINdir(PB9_GPIO_Port, PB9_Pin, 1);
			HAL_GPIO_WritePin(PB6_GPIO_Port, PB6_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(PB9_GPIO_Port, PB9_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB8_GPIO_Port, PB8_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(PB7_GPIO_Port, PB7_Pin, GPIO_PIN_RESET);

		}
	}
}





/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
	
	LED(1,1);		// wywoływanie funkcji "LED"
	HAL_Delay(500); // wywołanie opóźnienia czasowego
	LED(1,2);
	HAL_Delay(500);
	LED(1,3);
	HAL_Delay(500);
	LED(1,4);
	HAL_Delay(500);

	LED(2,1);
	HAL_Delay(500);
	LED(2,2);
	HAL_Delay(500);
	LED(2,3);
	HAL_Delay(500);
	LED(2,4);
	HAL_Delay(500);

	LED(3,1);
	HAL_Delay(500);
	LED(3,2);
	HAL_Delay(500);
	LED(3,3);
	HAL_Delay(500);
	LED(3,4);
	HAL_Delay(500);

	LED(4,1);
	HAL_Delay(500);
	LED(4,2);
	HAL_Delay(500);
	LED(4,3);
	HAL_Delay(500);
	LED(4,4);
	HAL_Delay(500);

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, PB6_Pin|PB9_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : B1_Pin */
  GPIO_InitStruct.Pin = B1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(B1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : LD2_Pin */
  GPIO_InitStruct.Pin = LD2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(LD2_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : PB6_Pin PB9_Pin */
  GPIO_InitStruct.Pin = PB6_Pin|PB9_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : PB7_Pin PB8_Pin */
  GPIO_InitStruct.Pin = PB7_Pin|PB8_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
