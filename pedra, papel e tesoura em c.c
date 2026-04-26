#include <stdio.h>
#include <string.h>

int main(){
//pedra papel tesoura

char player[256];
char player2[256];

printf("\nPlayer, sua vez de jogar!: ");
scanf("%s", player);

printf("\nPlayer2, sua vez!: ");
scanf("%s", player2);

printf("\nEstamos calculando o resultado...\n");

if(strcmp(player, "papel")==0){

    if(strcmp(player2, "papel")==0){
        printf("Empate!");
    }else if(strcmp(player2, "tesoura")==0){
        printf("Player 2 ganhou, porque tesoura corta papel!");
    }else if(strcmp(player2, "pedra")==0){
        printf("Player 2 perdeu, porque papel embrulha/ganha de pedra!");
    }else{
        printf("O player 2 jogou uma informacao invalida");
    }

}else if(strcmp(player, "tesoura")==0){

    if(strcmp(player2, "papel")==0){
        printf("Player 2 perdeu, porque tesoura corta papel!");
    }else if(strcmp(player2, "tesoura")==0){
        printf("Empate!");
    }else if(strcmp(player2, "pedra")==0){
        printf("Player 2 ganhou, porque pedra esmaga tesoura!");
    }else{
        printf("O player 2 jogou uma informacao invalida");
    }

}else if(strcmp(player, "pedra")==0){

    if(strcmp(player2, "papel")==0){
        printf("Player 2 ganhou, porque papel embrulha pedra!");
    }else if(strcmp(player2, "tesoura")==0){
        printf("Player 2 perdeu, porque pedra esmaga tesoura!");
    }else if(strcmp(player2, "pedra")==0){
        printf("Empate!");
    }else{
        printf("O player 2 jogou uma informacao invalida");
    }

}else{
    printf("Informacao invalida!");
}

return 0;
}