package awt_java_assignment;

import java.awt.*;
import java.awt.event.*;
import java.io.FileWriter;
import java.io.IOException;
// import pdf.pdfWriter;


class app{
    static class appWindow extends Frame{
        /**
         * Main app class
         */
        private static final long serialVersionUID = 1L;
        TextField name, qualification, personalDetails, hobbies;
        Label nameL, qualificationL, personalDetailsL, hobbiesL;
        GridBagLayout gridBag;
        GridBagConstraints constraints;
        appWindow(){

            gridBag = new GridBagLayout();
            constraints = new GridBagConstraints();

            name = new TextField(50);
            // nameL = 
            qualification = new TextField(50);
            // qualificationL = new Label("Qualifications:");
            personalDetails = new TextField(50);
            // personalDetailsL = new Label("Personal Details:");            
            hobbies = new TextField(50);
            // hobbiesL = new Label("Hobbies:");

            addConstraints(new Label("Name:"), 0, 0, 1, 1, 10, 1, GridBagConstraints.BOTH);
            addConstraints(name, 1, 0, 1, 1, 90, 0, GridBagConstraints.BOTH);
            addConstraints(new Label("Qualifications:"), 0, 1, 1, 1, 10, 20, GridBagConstraints.BOTH);
            addConstraints(qualification, 1, 1, 1, 1, 90, 0, GridBagConstraints.BOTH);
            addConstraints(new Label("Personal Details:"), 0, 2, 1, 1, 10, 20, GridBagConstraints.BOTH);
            addConstraints(personalDetails, 1, 2, 1, 1, 90, 0, GridBagConstraints.BOTH);
            addConstraints(new Label("Hobbies:"), 0, 3, 1, 1, 10, 20, GridBagConstraints.BOTH);
            addConstraints(hobbies, 1, 3, 1, 1, 90, 0, GridBagConstraints.BOTH);

            Button submit = new Button("Submit!");
            submit.addActionListener(new ActionListener(){ 
                public void actionPerformed(ActionEvent e) {
                    String nameValue = name.getText(),
                        qualificationValue = qualification.getText(),
                        personalDetailsValue = personalDetails.getText(),
                        hobbiesValue = hobbies.getText();
                    FileWriter pen = null;
                    try {
                        pen = new FileWriter("resume.txt");
                        pen.write("Name: " + nameValue + "\n");
                        pen.write("-------------------------------------------\n");
                        pen.write("qualifications: "+ qualificationValue+"\n");
                        pen.write("-------------------------------------------\n");
                        pen.write("personalDetails: "+ personalDetailsValue+"\n");
                        pen.write("-------------------------------------------\n");
                        pen.write("hobbies: "+ hobbiesValue+"\n");
                        pen.close();
                    } catch (IOException e1) {
                        System.out.print("An Error Occurred");
                    }
                    dispose();
                }
            });
            addConstraints(submit, 0, 4, 2, 1, 0, 1, GridBagConstraints.NONE);
            setLayout(gridBag);
            setSize(600, 600);          
            addWindowListener(new WindowAdapter(){  
                public void windowClosing(WindowEvent e) {  
                    dispose();  
                }  
            }); 
        }
        public void addConstraints(Component a, int gx, int gy,
                                        int gw, int gh, int wx, int wy, int fill){
            this.constraints.gridx = gx;
            this.constraints.gridy = gy;
            this.constraints.gridwidth = gw;
            this.constraints.gridheight = gh;
            this.constraints.weightx = wx;
            this.constraints.weighty = wy;
            this.constraints.fill = fill;            
            this.gridBag.setConstraints(a, this.constraints);
            this.add(a);
        }
    }
    
    public static void main(String[] args) throws IOException{
        appWindow mainWindow = new appWindow();
        mainWindow.setVisible(true);
    }
}