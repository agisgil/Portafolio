package modelo.vo;

public class Requerimiento_1Vo {
    private String ciudadResidencia;
    private Integer salarioPromedio;

    public Requerimiento_1Vo() {
    }

    public String getCiudadResidencia () {
        return ciudadResidencia;
    }

    public void setCiudadResidencia (String ciudadResidencia) {
        this.ciudadResidencia = ciudadResidencia;
    }

    public Integer getSalarioPromedio () {
        return salarioPromedio;
    }

    public void setSalarioPromedio (Integer salarioPromedio) {
        this.salarioPromedio = salarioPromedio;
    }

    @Override
    public String toString() {
        return ciudadResidencia + " " + salarioPromedio;
    }
}