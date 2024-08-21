/*-----------------------------------------------------------------------------
 Copyright (C) 2024 University of Bologna, Italy, ETH Zurich, Switzerland.
 All rights reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 See LICENSE.apache.md in the top directory for details.
 You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

 File:    uart_dma_setup.c
 Author:  Lorenzo Lamberti      <lorenzo.lamberti@unibo.it>
 Date:    01.03.2024
-------------------------------------------------------------------------------*/

#ifndef __UART_DMA_SETUP_H
#define __UART_DMA_SETUP_H

#include "uart_dma_pulp.h"

void USART_DMA_Start(uint32_t baudrate, int8_t *pulpRxBuffer, uint32_t BUFFERSIZE);
void USART_Reset_Buffer(int8_t *pulpRxBuffer);

#endif