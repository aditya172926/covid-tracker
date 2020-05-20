export class Patients
{
    Coronavirus_Cases: string;
    Deaths: string;
    Recovered: string;

    constructor(Coronavirus_Cases, Deaths, Recovered)
    {
        this.Coronavirus_Cases = Coronavirus_Cases;
        this.Deaths = Deaths;
        this.Recovered = Recovered;
    }
}