
import vista.VistaRequerimientos;
import vista.Ventana;

/**
 * Esta clase solo se debe usar para hacer pruebas locales, no se debe subir en
 * iMaster
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Requerimiento 1");
        VistaRequerimientos.requerimiento1();
        System.out.println();
        
        System.out.println("Requerimiento 2");
        VistaRequerimientos.requerimiento2();
        System.out.println();

        System.out.println("Requerimiento 3");
        VistaRequerimientos.requerimiento3();

        //public static void main(String[] args) {
            Ventana V = new Ventana();      // creamos una ventana
            V.setVisible(true);             // hacemos visible la ventana creada
        //}


    }
}
