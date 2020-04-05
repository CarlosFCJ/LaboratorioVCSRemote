package main
import (
        "fmt"
        "sort"
)
// En la funcion kello se crea el arreglo con los datos de 
func kello()([]int){
        kellos := []int{27834,23789,30189,30967,32501,32701,31665,17155,4614,834}
        return kellos
}
// Punto 1
//  Esta funcion saca promedios con los datos de kello dependiendo de los puntos que le indiquen para
// realiar los promedios, por ejemplo (0,5)
func promedio(r,t int)(int){
        m := kello()
        c := 0
        n := 0
        for p := r; p <=t; p++ {
                c = c + m[p]
                n = n + 1
        }
        prome := c / n
        return prome
}
// La funcion difer calcula diferencias entre promedios de 2 momentos
func difer(a1,b1,a2,b2 int)(int){
        prome1 := promedio(a1,b1)
        prome2 := promedio(a2,b2)
        dif := prome1 - prome2
        return dif
}
// Punto 2 +
// La funcion Dife calcula la deferencia entre el año que mayor se gano en kello y el que menor se gano
func dife()(int){
        mayor := mayorr()
        menor := menorr()
        Difr := mayor - menor
        return Difr
}
// La funcion menorr halla el dato de menor valor dentro de kello()
func menorr()(int){
        m := kello()
        menor := m[0]
        long := len(m)
        for p := 0; p <=(long-1); p++ { 
                if menor > (m[p]){ 
                        menor = m[p]
                }
        }
        return menor
}
// la funncion mayorr halla el dato de mayor valor dentro de kello()
func mayorr()(int){
        m := kello()
        mayor := m[0]
        long := len(m)
        for p := 0; p <=(long-1); p++ { 
                if mayor < (m[p]){ 
                        mayor = m[p]
                }
        }
        return mayor
}
// Punto 5
// En la funcion woo se realiza  una sumatoria para saber el valor total de todos lo valores dentro del arreglo kello
// para luego realizarce el promedio de que porcentaje aporto ese hallo al toltal.
func woo(){
        w := 0
        r := kello()
        long := len(r)
        a := 2008
        for n:=0; n<=(long-1);n = n+1 {
        w = w + r[n]
        }
        for c := 0; c<=(long-1);c = c+1 {
                f := r[c]
                por := (f*100)/w
                fmt.Print("El porcentaje que aporta el año ", a ,"es ",por ,"% \n")
                
                a = a + 1
        }
}
// punto 6
//  en la funcion woo se hace una sumatoria de los dijitos dentro del arreglo kello
// para luego procesar a sacar el deficit del año 2016 y 2017
func defi(){
        r := kello()
        long := len(r)
        D2017 := r[(long-1)]
        D2016 := r[(long-2)]
        deficits := D2016-D2017
        fmt.Print("El deficit del 2017 comparado con el de el 2016 es de ",deficits," cop")
}
// Punto 7 , la funcion calcula el deficits que hubo en la empresa por año
func deficis(){
        r := kello()
        long := len(r)
        A := 2017
        for i:=0; i <=9;i = i+1 {
                ult := (r[long-1])
                defi :=(r[long-2] - ult)
                ult2 := float64(ult)
                degi := float64(defi)
                defiporce := float64((degi*100)/ult2)
                long = long-1
                fmt.Print("el deficit en porcenta del año ",A," es ",defiporce," % \n")
                A = A - 1
        }
}
//punto 3 y 4 fue realizado dentro de main, por que al realizarlo como funcion me bota un fallo en el retorno.
// la funcion main es el corazon de la aplicacion y en la que se manda a ejecuta todo para que se muestre o realice
func main(){
        f := promedio(0,9)
        fmt.Println("El promedios es ", f)
        r := difer(0,1,8,9)
        fmt.Println("La diferencia entre los primeros años y los ultimos registrados es ", r)
        m := dife()
        fmt.Println("la diferencia entre la utilidad del año de mayor y la de menor es ", m)
        re := kello()
        sort.Ints(re)
        mr := len(re)
        v := mr%2 
        if v == 0 {
                mr = (mr/2)-1
                p1 := re[mr]
                p2 := re[(mr+1)]
                mg := (p1 + p2)/2
                fmt.Println("La mediana es ",mg)
                media := promedio(0,9)
                fmt.Println("La mediana es ",mg)
                fmt.Println("La media es ",media)
                if  media < mg{
                        FR := mg - media 
                        fmt.Println("es mas grande la media por ",FR)
                }
        }     
        woo()
        defi()
        deficis()
}