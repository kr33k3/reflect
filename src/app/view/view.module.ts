import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { MemoryModule } from '../memory/memory.module';


import { IonicModule } from '@ionic/angular';

import { MemoryNewComponent } from '../memory/memory-new/memory-new.component';
import { ViewPage } from './view.page';

const routes: Routes = [
  {
    path: '',
    component: ViewPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes),
    MemoryModule
  ],
  declarations: [ViewPage],
  entryComponents: [MemoryNewComponent]
})
export class ViewPageModule {}
