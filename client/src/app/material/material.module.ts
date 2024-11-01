import { NgModule } from "@angular/core";

// material modules
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from '@angular/material/input';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatSliderModule } from '@angular/material/slider';
import { MatDividerModule } from '@angular/material/divider';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatChipsModule } from '@angular/material/chips'
import { MatDialogModule } from '@angular/material/dialog';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';

const MATERIAL_MODULES = [

    MatToolbarModule,       MatButtonModule,
    MatIconModule,          MatMenuModule,
    MatSelectModule,        MatFormFieldModule,
    MatInputModule,         MatGridListModule,
    MatSliderModule,        MatDividerModule,
    MatCheckboxModule,      MatTooltipModule,
    MatPaginatorModule,     MatProgressSpinnerModule,
    MatChipsModule,         MatDialogModule,
    MatSlideToggleModule

]

@NgModule({
    imports: MATERIAL_MODULES,
    exports: MATERIAL_MODULES
})

export class MaterialModule{};