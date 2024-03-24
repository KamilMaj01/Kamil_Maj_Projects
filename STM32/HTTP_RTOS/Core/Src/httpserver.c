
/* Includes ------------------------------------------------------------------*/
#include "lwip/opt.h"
#include "lwip/arch.h"
#include "lwip/api.h"
#include "lwip/apps/fs.h"
#include "string.h"
#include <stdio.h>
#include "httpserver.h"
#include "cmsis_os.h"
#include "main.h"
#include "Servo.h"

const static char http_html_hdr[] = "HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n";
const static char http_html_hdr_to_value[] = "HTTP/1.1 200 OK\r\n\r\n";
const static char http_html_hdr_not_found[] = "HTTP/1.1 404 Not Found\r\nContent-type: text/html; charset=utf-8\r\n\r\n";



static void http_server(struct netconn *conn)
{
	struct netbuf *inbuf;
	err_t recv_err;
	char* buf;
	u16_t buflen;
	struct fs_file file;

	/* Read the data from the port, blocking if nothing yet there */
	recv_err = netconn_recv(conn, &inbuf);

	if (recv_err == ERR_OK)
	{
		if (netconn_err(conn) == ERR_OK)
		{
			/* Get the data pointer and length of the data inside a netbuf */
			netbuf_data(inbuf, (void**)&buf, &buflen);

			/* Check if request to get the index.html */
			if (strncmp((char const *)buf,"GET /index.html",15)==0)
			{
				fs_open(&file, "/index.html");
				netconn_write(conn, http_html_hdr, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);
				netconn_write(conn, (const unsigned char*)(file.data), (size_t)file.len, NETCONN_NOCOPY);
				fs_close(&file);

			}
			// Wypisywanie temperatury procesora na server
			else if(strncmp((char const *)buf,"GET /Temperature_value_procesor",31)==0){
				char *TempValue;
				TempValue = pvPortMalloc(30);
				size_t n = sprintf(TempValue, "%s%.1f C",http_html_hdr_to_value,Processor_temperature);
				netconn_write(conn,TempValue, n,NETCONN_NOCOPY);
				vPortFree(TempValue);
			}
			// Wypisywanie temperatury procesora na server
			else if(strncmp((char const *)buf,"GET /Temperature_value_room",27)==0){
				char *TempValue;
				TempValue = pvPortMalloc(30);
				size_t n = sprintf(TempValue, "%s%.1f C",http_html_hdr_to_value,Room_temperature);
				netconn_write(conn,TempValue, n,NETCONN_NOCOPY);
				vPortFree(TempValue);
			}
			// Wypisywanie Zadanego/akctulnego kąta servwomechanizmu na serwer
			else if(strncmp((char const *)buf,"GET /Angle_value",16)==0){
				char *AngleValue;
				AngleValue = pvPortMalloc(30);
				size_t n = sprintf(AngleValue, "%s%d",http_html_hdr_to_value,Actual_angle_value);
				netconn_write(conn,(const unsigned char*)AngleValue, n,NETCONN_NOCOPY);
				vPortFree(AngleValue);

			}
			//Ustawianie Ledów
			else if(strncmp((char const *)buf,"POST /buttoncolor=G_clicked",27)==0){
				HAL_GPIO_WritePin(LED2_GPIO_Port, LED2_Pin, GPIO_PIN_SET);
//				netconn_write(conn, http_html_hdr_to_value, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);

			}else if(strncmp((char const *)buf,"POST /buttoncolor=G_unclicked",29)==0){
				HAL_GPIO_WritePin(LED2_GPIO_Port, LED2_Pin, GPIO_PIN_RESET);
//				netconn_write(conn, http_html_hdr_to_value, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);

			}else if(strncmp((char const *)buf,"POST /buttoncolor=B_clicked",27)==0){
				HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_SET);
//				netconn_write(conn, http_html_hdr_to_value, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);

			}else if(strncmp((char const *)buf,"POST /buttoncolor=B_unclicked",29)==0){
				HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_RESET);
//				netconn_write(conn, http_html_hdr_to_value, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);

			}else if(strncmp((char const *)buf,"POST /buttoncolor=R_clicked",27)==0){
				HAL_GPIO_WritePin(LED3_GPIO_Port, LED3_Pin, GPIO_PIN_SET);
//				netconn_write(conn, http_html_hdr_to_value, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);

			}else if(strncmp((char const *)buf,"POST /buttoncolor=R_unclicked",29)==0){
				HAL_GPIO_WritePin(LED3_GPIO_Port, LED3_Pin, GPIO_PIN_RESET);
//				netconn_write(conn, http_html_hdr_to_value, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);
			}
			// Zadawanie konta serwomechanizm
			else if(strncmp((char const *)buf,"POST /Servo_angle",17)==0){
				char angle[3];
				for(size_t i = 0; i<3; i++){
					angle[i] = buf[i+18];
				}
				Actual_angle_value = (uint8_t)strtoul( angle, NULL, 0 );
				Servo_set_angle(Actual_angle_value);



			}


			else{
				/* Load Error page */
				fs_open(&file, "/404.html");
				netconn_write(conn, http_html_hdr_not_found, sizeof(http_html_hdr)-1, NETCONN_NOCOPY);
				netconn_write(conn, (const unsigned char*)(file.data), (size_t)file.len, NETCONN_NOCOPY);
				fs_close(&file);


			}







		}
	}
	/* Close the connection (server closes in HTTP) */
	netconn_close(conn);

	/* Delete the buffer (netconn_recv gives us ownership,
   so we have to make sure to deallocate the buffer) */
	netbuf_delete(inbuf);
}


static void http_thread(void *arg)
{ 
  struct netconn *conn, *newconn;
  err_t err, accept_err;
  
  /* Create a new TCP connection handle */
  conn = netconn_new(NETCONN_TCP);
  
  if (conn!= NULL)
  {
    /* Bind to port 80 (HTTP) with default IP address */
    err = netconn_bind(conn, IP_ADDR_ANY, 80);
    
    if (err == ERR_OK)
    {
      /* Put the connection into LISTEN state */
      netconn_listen(conn);
  
      while(1) 
      {
        /* accept any incoming connection */
        accept_err = netconn_accept(conn, &newconn);
        if(accept_err == ERR_OK)
        {
          /* serve connection */
          http_server(newconn);

          /* delete connection */
          netconn_delete(newconn);
        }
      }
    }
  }
}


void http_server_init()
{
  sys_thread_new("http_thread", http_thread, NULL, 2*DEFAULT_THREAD_STACKSIZE, osPriorityNormal);
}


