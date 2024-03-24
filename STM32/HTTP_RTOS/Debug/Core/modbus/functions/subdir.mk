################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/modbus/functions/mbfunccoils.c \
../Core/modbus/functions/mbfuncdiag.c \
../Core/modbus/functions/mbfuncdisc.c \
../Core/modbus/functions/mbfuncholding.c \
../Core/modbus/functions/mbfuncinput.c \
../Core/modbus/functions/mbfuncother.c \
../Core/modbus/functions/mbutils.c 

OBJS += \
./Core/modbus/functions/mbfunccoils.o \
./Core/modbus/functions/mbfuncdiag.o \
./Core/modbus/functions/mbfuncdisc.o \
./Core/modbus/functions/mbfuncholding.o \
./Core/modbus/functions/mbfuncinput.o \
./Core/modbus/functions/mbfuncother.o \
./Core/modbus/functions/mbutils.o 

C_DEPS += \
./Core/modbus/functions/mbfunccoils.d \
./Core/modbus/functions/mbfuncdiag.d \
./Core/modbus/functions/mbfuncdisc.d \
./Core/modbus/functions/mbfuncholding.d \
./Core/modbus/functions/mbfuncinput.d \
./Core/modbus/functions/mbfuncother.d \
./Core/modbus/functions/mbutils.d 


# Each subdirectory must supply rules for building sources it contributes
Core/modbus/functions/%.o Core/modbus/functions/%.su Core/modbus/functions/%.cyclo: ../Core/modbus/functions/%.c Core/modbus/functions/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F429xx -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I../LWIP/App -I../LWIP/Target -I../Middlewares/Third_Party/LwIP/src/include -I../Middlewares/Third_Party/LwIP/system -I../Middlewares/Third_Party/FreeRTOS/Source/include -I../Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../Drivers/BSP/Components/lan8742 -I../Middlewares/Third_Party/LwIP/src/include/netif/ppp -I../Middlewares/Third_Party/LwIP/src/apps/http -I../Middlewares/Third_Party/LwIP/src/include/lwip -I../Middlewares/Third_Party/LwIP/src/include/lwip/apps -I../Middlewares/Third_Party/LwIP/src/include/lwip/priv -I../Middlewares/Third_Party/LwIP/src/include/lwip/prot -I../Middlewares/Third_Party/LwIP/src/include/netif -I../Middlewares/Third_Party/LwIP/src/include/compat/posix -I../Middlewares/Third_Party/LwIP/src/include/compat/posix/arpa -I../Middlewares/Third_Party/LwIP/src/include/compat/posix/net -I../Middlewares/Third_Party/LwIP/src/include/compat/posix/sys -I../Middlewares/Third_Party/LwIP/src/include/compat/stdc -I../Middlewares/Third_Party/LwIP/system/arch -I../Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS -I../Core/modbus/tcp -I../Core/modbus/include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-modbus-2f-functions

clean-Core-2f-modbus-2f-functions:
	-$(RM) ./Core/modbus/functions/mbfunccoils.cyclo ./Core/modbus/functions/mbfunccoils.d ./Core/modbus/functions/mbfunccoils.o ./Core/modbus/functions/mbfunccoils.su ./Core/modbus/functions/mbfuncdiag.cyclo ./Core/modbus/functions/mbfuncdiag.d ./Core/modbus/functions/mbfuncdiag.o ./Core/modbus/functions/mbfuncdiag.su ./Core/modbus/functions/mbfuncdisc.cyclo ./Core/modbus/functions/mbfuncdisc.d ./Core/modbus/functions/mbfuncdisc.o ./Core/modbus/functions/mbfuncdisc.su ./Core/modbus/functions/mbfuncholding.cyclo ./Core/modbus/functions/mbfuncholding.d ./Core/modbus/functions/mbfuncholding.o ./Core/modbus/functions/mbfuncholding.su ./Core/modbus/functions/mbfuncinput.cyclo ./Core/modbus/functions/mbfuncinput.d ./Core/modbus/functions/mbfuncinput.o ./Core/modbus/functions/mbfuncinput.su ./Core/modbus/functions/mbfuncother.cyclo ./Core/modbus/functions/mbfuncother.d ./Core/modbus/functions/mbfuncother.o ./Core/modbus/functions/mbfuncother.su ./Core/modbus/functions/mbutils.cyclo ./Core/modbus/functions/mbutils.d ./Core/modbus/functions/mbutils.o ./Core/modbus/functions/mbutils.su

.PHONY: clean-Core-2f-modbus-2f-functions

