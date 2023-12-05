import mongoose from "mongoose";

const appointmentSchema = new mongoose.Schema({
  name: String,
  cpf: String,
  phone: String,
  email: String,
  country: String,
  state: String,
  cep: String,
  street: String,
  neighborhood: String,
  complement: String,
  specialty: String,
  clinic: String,
  insurance: String,
  date: String,
  time: String,
});

export const AppointmentModel = mongoose.model("Appointment", appointmentSchema);
