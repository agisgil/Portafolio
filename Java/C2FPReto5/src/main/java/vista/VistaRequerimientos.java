package vista;

import java.util.ArrayList;

import controlador.ControladorRequerimientos;
import modelo.vo.Requerimiento_1Vo;
import modelo.vo.Requerimiento_2Vo;
import modelo.vo.Requerimiento_3Vo;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;
import javax.swing.ButtonGroup;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

public class VistaRequerimientos extends JFrame implements ActionListener {

    public static final ControladorRequerimientos controlador = new ControladorRequerimientos();

    private JLabel texto; // etiqueta o texto no editable
    private JRadioButton rb1, rb2, rb3; // Radio Boton por cada consulta
    private ButtonGroup bg; // Grupo de Radio Boton
    private JButton boton; // boton ejecucion de consulta
    
    public VistaRequerimientos() {
        super();                    // usamos el contructor de la clase padre JFrame
        configurarVentana();        // configuramos la ventana
        inicializarComponentes();   // inicializamos los atributos o componentes
    }

    private void configurarVentana() {
        this.setTitle("Reto 5 - Ventana Consultas - Adriana Gislena Gil");  // titulo de la ventana
        this.setSize(550, 250);            // tamaño de la ventana (ancho, alto)
        //this.setLocation(400, 20);
        this.setLocationRelativeTo(null);  // centrar la ventana en la pantalla
        this.setLayout(null);              // no usamos ningun layout, solo asi podremos dar posiciones a los componentes
        this.setResizable(false);          // hacer que la ventana no sea redimiensionable
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  // hacer que cuando se cierre la ventana termina todo proceso
    }

    private void inicializarComponentes() {
        texto = new JLabel("SELECCIONE LA CONSULTA:");
        texto.setBounds(20, 20, 200, 25);   // posicion y tamanio al texto (x, y, ancho, alto)
        rb1 = new JRadioButton("Promedio Salarios de Líderes de Proyecto, Agrupados por Ciudad de Residencia", false);
        rb1.setActionCommand("1");
        rb1.setBounds(20, 50, 800, 25);
        rb2 = new JRadioButton("Proveedores de Compras Realizadas para Proyectos en Neiva", false);
        rb2.setActionCommand("2");
        rb2.setBounds(20, 75, 800, 25);
        rb3 = new JRadioButton("Materiales utilizados en Proyectos con ID entre 40 y 55, orden ascendente", false); 
        rb3.setActionCommand("3");
        rb3.setBounds(20, 100, 800, 25);
        bg = new ButtonGroup();    
        bg.add(rb1); bg.add(rb2); bg.add(rb3);
        boton = new JButton("CONSULTAR");
        boton.setBounds(180, 150, 130, 30);  
        boton.addActionListener(this);  // hacer que el boton tenga una accion y esa accion estara en esta clase
                        
        // adicionamos los componentes a la ventana
        this.add(texto);
        this.add(rb1); this.add(rb2); this.add(rb3);    
        this.add(boton);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (rb1.isSelected()) {
            requerimiento1();
        }    
        if (rb2.isSelected()) {    
            requerimiento2();    
        }  
        if (rb3.isSelected()) {    
            requerimiento3();   
        } 
        bg.clearSelection();
    }

    public static void requerimiento1() {
        try {
            // Obtener datos de la tabla
            ArrayList<Requerimiento_1Vo> resultado_requerimiento1 = controlador.consultarRequerimiento1();

            DefaultTableModel modelo = new DefaultTableModel();
            String[] columnas = {"Ciudad_Residencia", "Promedio"};
            modelo.setColumnIdentifiers(columnas);
                
            for (Requerimiento_1Vo i : resultado_requerimiento1) {
                modelo.addRow(new Object[] {i.getCiudadResidencia(), i.getSalarioPromedio()});
            }

            JFrame frame = new JFrame();
            JTable tabla = new JTable();
            tabla.setModel(modelo);
            tabla.setAutoResizeMode(JTable.AUTO_RESIZE_ALL_COLUMNS);
            tabla.setFillsViewportHeight(true);
            JScrollPane sp = new JScrollPane(tabla,JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);    
            frame.add(sp);
            frame.setTitle("PROMEDIO SALARIO LIDERES");
            frame.setSize(400, 250);
            frame.setLocationRelativeTo(null);    
            frame.setVisible(true);    
                
        } catch (Exception e) {
            JFrame mensaje = new JFrame();
            JOptionPane.showMessageDialog(mensaje, "Se ha producido el siguiente error:" + e.getMessage());
            //e.printStackTrace();
        }
    }

    public static void requerimiento2() {
        try {
            // Obtener datos de la tabla
            ArrayList<Requerimiento_2Vo> resultado_requerimiento2 = controlador.consultarRequerimiento2();

            DefaultTableModel modelo = new DefaultTableModel();
            String[] columnas = {"ID_Proyecto", "Proveedor"};
            modelo.setColumnIdentifiers(columnas);
                
            for (Requerimiento_2Vo i : resultado_requerimiento2) {
                modelo.addRow(new Object[] {i.getIdProyecto(), i.getProveedor()});
            }

            JFrame frame = new JFrame();
            JTable tabla = new JTable();
            tabla.setModel(modelo);
            tabla.setAutoResizeMode(JTable.AUTO_RESIZE_ALL_COLUMNS);
            tabla.setFillsViewportHeight(true);
            JScrollPane sp = new JScrollPane(tabla,JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);    
            frame.add(sp);
            frame.setTitle("PROVEEDORES PROYECTOS NEIVA");
            frame.setSize(400, 250);
            frame.setLocationRelativeTo(null);    
            frame.setVisible(true);    
                
        } catch (Exception e) {
            JFrame mensaje = new JFrame();
            JOptionPane.showMessageDialog(mensaje, "Se ha producido el siguiente error:" + e.getMessage());
            //e.printStackTrace();
        }
    }

    
    public static void requerimiento3() {
        try {
            // Obtener datos de la tabla
            ArrayList<Requerimiento_3Vo> resultado_requerimiento3 = controlador.consultarRequerimiento3();

            DefaultTableModel modelo = new DefaultTableModel();
            String[] columnas = {"ID_Proyecto", "Nombre_Material"};
            modelo.setColumnIdentifiers(columnas);
                
            for (Requerimiento_3Vo i : resultado_requerimiento3) {
                modelo.addRow(new Object[] {i.getIdProyecto(), i.getNombreMaterial()});
            }

            JFrame frame = new JFrame();
            JTable tabla = new JTable();
            tabla.setModel(modelo);
            tabla.setAutoResizeMode(JTable.AUTO_RESIZE_ALL_COLUMNS);
            tabla.setFillsViewportHeight(true);
            JScrollPane sp = new JScrollPane(tabla,JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);    
            frame.add(sp);
            frame.setTitle("MATERIALES PROYECTOS ID 40 AL 45");
            frame.setSize(400, 250);
            frame.setLocationRelativeTo(null);    
            frame.setVisible(true);    
                
        } catch (Exception e) {
            JFrame mensaje = new JFrame();
            JOptionPane.showMessageDialog(mensaje, "Se ha producido el siguiente error:" + e.getMessage());
            //e.printStackTrace();
        }
    }
}