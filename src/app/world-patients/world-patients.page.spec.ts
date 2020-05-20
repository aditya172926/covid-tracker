import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { WorldPatientsPage } from './world-patients.page';

describe('WorldPatientsPage', () => {
  let component: WorldPatientsPage;
  let fixture: ComponentFixture<WorldPatientsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorldPatientsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(WorldPatientsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
