#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<time.h>
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
int hour = -01;
int min = 00;
int sec = 00; 
void *hourThread(void *vargp){
	if(hour == -01 || min == 05){
		pthread_mutex_lock(&mutex1);
		hour = hour + 1;
		min = 00;
		sec = 00;
		pthread_mutex_unlock(&mutex1);
	}
	return NULL;
}

void *minThread(void *vargp){
	if(min <= 5){
		pthread_mutex_lock(&mutex1);
		sleep(1);
		min = min + 01;
		sec = 00;		
		pthread_mutex_unlock(&mutex1);
	}
	return NULL;
}

void *secThread(void *vargp){
	while(sec != 5){
		pthread_mutex_lock(&mutex1);
		sleep(1);
		printf("\n%d", hour);
		printf(":%d", min);
		printf(":%d", sec);
		sec =  sec + 01;	
		pthread_mutex_unlock(&mutex1);
	}
	return NULL;
}

int main(){
	pthread_t thread_id1, thread_id2, thread_id3;
	printf("The Clock is Started\n");
	while(1){
		pthread_create(&thread_id1, NULL, hourThread, NULL);
		sleep(1);
		pthread_create(&thread_id2, NULL, minThread, NULL);	
		sleep(1);
		pthread_create(&thread_id3, NULL, secThread, NULL);
		sleep(1);
		pthread_join(thread_id1, NULL);
		pthread_join(thread_id2, NULL);
		pthread_join(thread_id3, NULL);
		//printf("\nAfter Thread");
	}
	exit(0);
}
