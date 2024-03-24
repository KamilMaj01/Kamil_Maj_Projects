################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Modbus/functions/mbfunccoils.c \
../Modbus/functions/mbfuncdiag.c \
../Modbus/functions/mbfuncdisc.c \
../Modbus/functions/mbfuncholding.c \
../Modbus/functions/mbfuncinput.c \
../Modbus/functions/mbfuncother.c \
../Modbus/functions/mbutils.c 

OBJS += \
./Modbus/functions/mbfunccoils.o \
./Modbus/functions/mbfuncdiag.o \
./Modbus/functions/mbfuncdisc.o \
./Modbus/functions/mbfuncholding.o \
./Modbus/functions/mbfuncinput.o \
./Modbus/functions/mbfuncother.o \
./Modbus/functions/mbutils.o 

C_DEPS += \
./Modbus/functions/mbfunccoils.d \
./Modbus/functions/mbfuncdiag.d \
./Modbus/functions/mbfuncdisc.d \
./Modbus/functions/mbfuncholding.d \
./Modbus/functions/mbfuncinput.d \
./Modbus/functions/mbfuncother.d \
./Modbus/functions/mbutils.d 


# Each subdirectory must supply rules for building sources it contributes
Modbus/functions/%.o Modbus/functions/%.su Modbus/functions/%.cyclo: ../Modbus/functions/%.c Modbus/functions/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F429xx -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I../LWIP/App -I../LWIP/Target -I../Middlewares/Third_Party/LwIP/src/include -I../Middlewares/Third_Party/LwIP/system -I../Middlewares/Third_Party/FreeRTOS/Source/include -I../Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../Drivers/BSP/Components/lan8742 -I../Middlewares/Third_Party/LwIP/src/include/netif/ppp -I../Middlewares/Third_Party/LwIP/src/apps/http -I../Middlewares/Third_Party/LwIP/src/include/lwip -I../Middlewares/Third_Party/LwIP/src/include/lwip/apps -I../Middlewares/Third_Party/LwIP/src/include/lwip/priv -I../Middlewares/Third_Party/LwIP/src/include/lwip/prot -I../Middlewares/Third_Party/LwIP/src/include/netif -I../Middlewares/Third_Party/LwIP/src/include/compat/posix -I../Middlewares/Third_Party/LwIP/src/include/compat/posix/arpa -I../Middlewares/Third_Party/LwIP/src/include/compat/posix/net -I../Middlewares/Third_Party/LwIP/src/include/compat/posix/sys -I../Middlewares/Third_Party/LwIP/src/include/compat/stdc -I../Middlewares/Third_Party/LwIP/system/arch -I../Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS -I"C:/Users/majka/STM32CubeIDE/workspace_1.13.2/HTTP_RTOS/Modbus/include" -I"C:/Users/majka/STM32CubeIDE/workspace_1.13.2/HTTP_RTOS/Modbus/tcp" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Modbus-2f-functions

clean-Modbus-2f-functions:
	-$(RM) ./Modbus/functions/mbfunccoils.cyclo ./Modbus/functions/mbfunccoils.d ./Modbus/functions/mbfunccoils.o ./Modbus/functions/mbfunccoils.su ./Modbus/functions/mbfuncdiag.cyclo ./Modbus/functions/mbfuncdiag.d ./Modbus/functions/mbfuncdiag.o ./Modbus/functions/mbfuncdiag.su ./Modbus/functions/mbfuncdisc.cyclo ./Modbus/functions/mbfuncdisc.d ./Modbus/functions/mbfuncdisc.o ./Modbus/functions/mbfuncdisc.su ./Modbus/functions/mbfuncholding.cyclo ./Modbus/functions/mbfuncholding.d ./Modbus/functions/mbfuncholding.o ./Modbus/functions/mbfuncholding.su ./Modbus/functions/mbfuncinput.cyclo ./Modbus/functions/mbfuncinput.d ./Modbus/functions/mbfuncinput.o ./Modbus/functions/mbfuncinput.su ./Modbus/functions/mbfuncother.cyclo ./Modbus/functions/mbfuncother.d ./Modbus/functions/mbfuncother.o ./Modbus/functions/mbfuncother.su ./Modbus/functions/mbutils.cyclo ./Modbus/functions/mbutils.d ./Modbus/functions/mbutils.o ./Modbus/functions/mbutils.su

.PHONY: clean-Modbus-2f-functions

