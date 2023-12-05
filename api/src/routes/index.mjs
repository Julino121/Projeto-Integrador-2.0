import { Router } from "express";

import { appointmentsRoutes } from "./appointments.mjs";

const routes = Router();

routes.use("/appointments", appointmentsRoutes);

export { routes };
