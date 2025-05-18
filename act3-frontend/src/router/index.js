import { createRouter, createWebHistory } from 'vue-router';
import PatientManagement from '../components/PatientManagement.vue';
import MedicalRecords from '../components/MedicalRecords.vue';

const routes = [
    {
        path: '/',
        name: 'PatientManagement',
        component: PatientManagement,
    },
    {
        path: '/patients/:patientId/records',
        name: 'MedicalRecords',
        component: MedicalRecords,
        props: true, 
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;