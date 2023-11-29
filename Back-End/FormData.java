public class FormData {
    private PersonalInfo personalInfo;
    private Address address;
    private Appointment appointment;
    
    public static class PersonalInfo {
        private String nome;
        private String cpf;
        private String celular;
        private String email;

        // getters and setters
    }

    public static class Address {
        private String cep;
        private String rua;

        // getters and setters
    }

    public static class Appointment {
        private String especialidae;
        private String clinica;
        private String convenio;
        private String data;
        private String horario;

        // getters and setters
    }
}