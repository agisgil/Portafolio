public class App{
    public static void main(String[] args) {
        Lasanas[] Lasanas1 = new Lasanas[5];
        Lasanas1[0] = new Lasanas("carne","4_porciones",22000.0);
        Lasanas1[1] = new ExtraQueso("pollo","12_porciones",25000.0, "provolone");
        Lasanas1[2] = new ExtraVegetales("camarones","12_porciones",18000.0, "champiñones");
        Lasanas1[3] = new ExtraVegetales("espinaca","4_porciones",25000.0, "calabacitas");
        Lasanas1[4] = new Lasanas();
        ValorTotal respuesta1 = new ValorTotal(Lasanas1);
        respuesta1.mostrarTotales();
        System.out.println();
        System.out.println("------------------------");
        Lasanas[] Lasanas2 = new Lasanas[4];
        Lasanas2[0] = new Lasanas();
        Lasanas2[1] = new Lasanas("pollo","12_porciones",23000.0);
        Lasanas2[2] = new ExtraQueso("espinaca","4_porciones",25000.0, "suizo");
        Lasanas2[3] = new ExtraVegetales("carne","12_porciones",23000.0, "calabacitas");
        ValorTotal respuesta2 = new ValorTotal(Lasanas2);
        respuesta2.mostrarTotales();
        System.out.println();
    }
}
// 60600  -  50000  -  80700  -  191300
// 68600  -  39500  -  47900  -  156000

class Lasanas {
    // Constantes
    private final static Double PRECIOBASE = 20000.0;
    private final static String SABOR="pollo";
    private final static String TAMANO="1_porcion";

    // Atributos
    private String sabor;
    private String tamano;
    private Double precioBase;

    // Constructores
    public Lasanas() {
        this.sabor = SABOR;
        this.tamano = TAMANO;
        this.precioBase = PRECIOBASE;
    }
    public Lasanas(String sabor, String tamano, Double precioBase) {
        this.sabor = sabor;
        this.tamano = tamano;
        this.precioBase = precioBase;
    }

    //getter and setter
    public String getSabor() {
        return sabor;
    }
    public void setSabor(String sabor) {
        this.sabor = sabor;
    }

    public String getTamano() {
        return tamano;
    }
    public void setTamano(String tamano) {
        this.tamano = tamano;
    }

    public Double getPrecioBase() {
        return precioBase;
    }
    public void setPrecioBase(Double precioBase) {
        this.precioBase = precioBase;
    }

    //Métodos
    public double calcularPrecio() {
        if (sabor.equals("espinaca")) {
            precioBase += (precioBase*0.1);
        } else if (sabor.equals("pollo")) {
            precioBase += (precioBase*0.2);
        } else if (sabor.equals("carne")) {
            precioBase += (precioBase*0.3);
        } else if (sabor.equals("camarones")) {
            precioBase += (precioBase*0.4);
        } 

        if (tamano.equals("1_porcion")) {
            precioBase += 2000;
        } else if (tamano.equals("4_porciones")) {
            precioBase += 6000;
        } else if (tamano.equals("12_porciones")) {
            precioBase += 15000;
        } 

        return precioBase;
    }
}

class ExtraVegetales extends Lasanas {
    // Atributos
    private String tipoVegetales;

    // Constructor
    public ExtraVegetales(String sabor, String tamano, Double precioBase, String tipoVegetales) {
        super(sabor, tamano, precioBase);
        this.tipoVegetales = tipoVegetales;
    }

    //getter and setter
    public String gettipoVegetales() {
        return tipoVegetales;
    }
    public void settipoVegetales(String tipoVegetales) {
        this.tipoVegetales = tipoVegetales;
    }

    // Metodo
    @Override
    public double calcularPrecio() {
        int adicionar = 0;
        if (tipoVegetales.equals("calabacitas")){
            adicionar = 3000;
        }else if (tipoVegetales.equals("champiñones")){
            adicionar = 4000;
        }
        return super.calcularPrecio() + adicionar;
    }
}

class ExtraQueso extends Lasanas {
    // Atributo
    private String tipoQueso;

    // Constructor
    public ExtraQueso(String sabor, String tamano, Double precioBase, String tipoQueso) {
        super(sabor, tamano, precioBase);
        this.tipoQueso = tipoQueso;
    }

    //getter and setter
    public String gettipoQueso() {
        return tipoQueso;
    }
    public void settipoQueso(String tipoQueso) {
        this.tipoQueso = tipoQueso;
    }

    // Metodo
    @Override
    public double calcularPrecio() {
        int adicionar = 0;
        if(tipoQueso.equals("provolone")){
            adicionar = 5000;
        }else if (tipoQueso.equals("suizo")){
            adicionar = 6000;
        }
        return super.calcularPrecio() + adicionar;
    }
}

class ValorTotal {
    // Atributos
    private Double valorTotalLasanas = 0.00;
    private Double valorTotalLasanasExtraQueso = 0.00;
    private Double valorTotalLasanasExtraVegetales = 0.00;
    private Lasanas[] lasanas;

    // Constructores
    public ValorTotal(Lasanas[] lasanas) {
        this.lasanas = lasanas;
    }    

    // Métodos
    public void mostrarTotales() {
        int i = 0;
        for (i = 0; i < lasanas.length; i++){
            switch (lasanas[i].getClass().getName()) {
                case "Lasanas":
                    valorTotalLasanas += lasanas[i].calcularPrecio();
                    break;
                case "ExtraQueso":
                    valorTotalLasanasExtraQueso += lasanas[i].calcularPrecio();
                    break;
                case "ExtraVegetales":
                    valorTotalLasanasExtraVegetales += lasanas[i].calcularPrecio();
                    break;
            }            
        }
        // Cálculo totales
        System.out.println(Math.round(valorTotalLasanas));
        System.out.println(Math.round(valorTotalLasanasExtraQueso));
        System.out.println(Math.round(valorTotalLasanasExtraVegetales));
        System.out.println(Math.round(valorTotalLasanas + valorTotalLasanasExtraQueso+ valorTotalLasanasExtraVegetales));
    }
}
