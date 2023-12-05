import { AppointmentModel } from "../models/appointment-model.js";

import { validationInServer } from '../utils/validationInServer.util.js';

export class AppointmentsService {
  async create(req, res, next, data) {
    try {
      const validationResponse = await validationInServer(data);
    
      if (validationResponse === 'INVALIDO') {
        res.statusCode = 400;

        var e = new Error('error message');
        next(e);

        return;
      }
      
      const newAppointment = new AppointmentModel(data);
      await newAppointment.save();

      return newAppointment;
    } catch (error) {
      console.error("Erro aso criar com promisso no serviço:", error);
      throw error;
    }
  }
}
